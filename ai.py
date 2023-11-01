# Steps:
# Set up file writing to ai.json
# Finish basic functions to manage ai.json
# Make sure bias accounts for wins, loses, and ties
# Remember, there is a random component to this
# Test it out manually, see the changes in ai.json
# Write either a random move player or smart player to play 1,000+ games so the ai learns how to play faster

from a4 import TTTBoard
import random
import json

def get_data():
    with open("ai.json", "r") as file:
        return json.load(file)


def post_data(data):
    with open("ai.json", "w") as file:
        json.dump(data, file)


def generate_moves(board):
    new_case = {
        "board": board,
        "possibleMoves": [],
    }
    for i in range(len(board)):
        if board[i] != "*": continue
        new_case["possibleMoves"].append({
            "move": i,
            "bias": 1
        })
    return new_case


def index_of_case(cases, board):
    for i in range(len(cases)):
        if cases[i]["board"] == board:
            return i
    return -1


def predict_move(board):
    data = get_data()
    index = index_of_case(data["cases"], board)
    if index == -1:
        index = len(data["cases"])
        data["cases"].append(generate_moves(board))
        post_data(data)
    possible_moves = data["cases"][index]["possibleMoves"]

    total_bias = 0
    for move in possible_moves:
        total_bias += move["bias"]
    random_bias = random.randint(1, total_bias)

    count = 0
    for move in possible_moves:
        if random_bias <= count + move["bias"]:
            return move["move"]
        count += move["bias"]


def find_move(before, after):
    for i in range(len(before)):
        if before[i] != after[i]:
            return i
    return -1


def update_bias(moves, mod):
    data = get_data()
    current_case = -1

    for i in range(len(moves)):
        if i % 2 == 0:
            # player move
            if i == len(moves) - 1: break
            current_case = index_of_case(data["cases"], moves[i])
            if current_case == -1:
                data["cases"].append(generate_moves(moves[i]))
                current_case = len(data["cases"]) - 1
        elif current_case != -1:
            # bot move
            for k in range(len(data["cases"][current_case]["possibleMoves"])):
                if data["cases"][current_case]["possibleMoves"][k]["move"] == find_move(moves[i - 1], moves[i]):
                    new_bias = data["cases"][current_case]["possibleMoves"][k]["bias"] + mod
                    if new_bias < 1: continue
                    data["cases"][current_case]["possibleMoves"][k]["bias"] = new_bias
    
    post_data(data)


def play_tic_tac_toe_with_ai() -> None:
    """Uses my cool ai to play TicTacToe"""

    def is_int(maybe_int: str):
        """Returns True if val is int, False otherwise

        Args:
            maybe_int - string to check if it's an int

        Returns:
            True if maybe_int is an int, False otherwise
        """
        try:
            int(maybe_int)
            return True
        except ValueError:
            return False

    brd = TTTBoard()
    players = ["X", "O"]
    turn = 0
    game_moves = []

    while not brd.game_over():
        print(brd)
        move_index: int = 0
        if turn == 0:
            move: str = input("Human, what is your move? ")
            if not is_int(move):
                raise ValueError(
                    f"Given invalid position {move}, position must be integer between 0 and 8 inclusive"
                )
            move_index = int(move)
        else:
            move_index = predict_move(brd.board)

        if brd.make_move(players[turn], move_index):
            turn = not turn
            game_moves.append(brd.board[:])

    print(f"\nGame over!\n\n{brd}")
    if brd.has_won(players[0]):
        print(f"Human wins!")
        update_bias(game_moves, -1)
    elif brd.has_won(players[1]):
        print(f"AI wins!")
        update_bias(game_moves, 2)
    else:
        print(f"Board full, cat's game!")
        update_bias(game_moves, 1)


def run_tic_tac_toe_with_ai(games: int) -> None:
    """Uses my cool ai to run TicTacToe games"""

    def make_random_move(board):
        random_value = random.randint(0, board.count("*") - 1)
        count = 0
        for i in range(len(board)):
            if board[i] == "*":
                if count == random_value:
                    return i
                count += 1


    for i in range(games):
        brd = TTTBoard()
        players = ["X", "O"]
        turn = 0
        moves = []

        while not brd.game_over():
            move_index: int = make_random_move(brd.board) if turn == 0 else predict_move(brd.board)
            if brd.make_move(players[turn], move_index):
                turn = not turn
                moves.append(brd.board[:])

        if brd.has_won(players[0]):
            print(f"Human wins!")
            update_bias(moves, -1)
        elif brd.has_won(players[1]):
            print(f"AI wins!")
            update_bias(moves, 2)
        else:
            print(f"Board full, cat's game!")
            update_bias(moves, 1)


play_tic_tac_toe_with_ai()
# run_tic_tac_toe_with_ai(1000)
