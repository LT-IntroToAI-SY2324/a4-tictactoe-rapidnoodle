# Steps:
# Set up file writing to ai.json
# Finish basic functions to manage ai.json
# Make sure bias accounts for wins, loses, and ties
# Remember, there is a random component to this
# Test it out manually, see the changes in ai.json
# Write either a random move player or smart player to play 1,000+ games so the ai learns how to play faster

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
        moved = board[:]
        moved[i] = "O"
        new_case["possibleMoves"].append({
            "move": moved,
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
    # pick back up here


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
                if data["cases"][current_case]["possibleMoves"][k]["move"] == moves[i]:
                    data["cases"][current_case]["possibleMoves"][k]["bias"] += mod
    
    post_data(data)


# print(generate_moves(["*", "*", "*"]))

moves = [
    ["X", "*", "*"],
    ["X", "O", "*"],
    ["X", "O", "X"]
]
# update_bias(moves, 1)
print(get_data())

# {
#     "wins": 0,
#     "loses": 0,
#     "ties": 0,
#     "cases": [
#         {
#             "board": ["*", "*", "*"],
#             "possibleMoves": [
#                 {
#                     "move": ["X", "*", "*"],
#                     "bias": 1
#                 }
#             ]
#         }
#     ]
# }
