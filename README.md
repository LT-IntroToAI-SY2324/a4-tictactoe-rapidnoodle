---
title: 'Assignment 4: Tic Tac Toe'
author: |
  | Assignment written by Christine Alvarado, Harvey Mudd College,
  | with changes by Nathan Shelly and Sara Sood, Northwestern University.
geometry: margin=1in
---

In this assignment you will develop a class for managing a game of Tic Tac Toe. While we covered the basics of creating classes in Python in class, you will probably want to refer back to your notes and to Python's documentation on creating classes.

Create a class called `TTTBoard` that defines the following functions:

- `__init__(self)`: Initialize a 3x3 tic tac toe board. The board should contain a single attribute, a list called `board`, that initially contains nine `'*'` characters. This list contains the contents of the board. A `'*'` denotes that this position has not yet been claimed by 'X' or 'O'. Again, this is simply a flat list of 9 items, not a list of lists. 
- `__str__(self)`: Returns a string representation of the board. Instead of just displaying a flat list of the 9 items, we want to display it like a tic tac toe board, with 3 rows of 3 items each. For example, here is what the board would look like after player "X" plays 3 and player "O" plays 6:

  ```text
  * * *
  X * *
  O * *
  ```

  _Hint:_ use `\n` to insert a new line, for example try the following in the Python interpreter:

  ```python
    >>> print("Hello\nWorld")
    Hello
    World
  ```

- `make_move(self, player, pos)`: Places a move for `player` in the position `pos` (where the board squares are numbered from left to right, starting in the top left square with 0, and beginning at the left in each new row), if possible. '`player`' is a string ("X" or "O") and `pos` is an integer. Returns `True` if the move was made and `False` if not (because the spot was full, or outside the boundaries of the board).
- `has_won(self, player)`: Returns `True` if `player` has won the game, and `False` if not
- `game_over(self)`: Returns `True` if someone has won or if the board is full, `False` otherwise
- `clear(self)`: Clears the board to reset the game

You may define other methods as well, but those listed above are all that are required.

To help you to ensure that your code is working properly, we have provided 2 additional things:

1. A function (called `play_tic_tac_toe`) outside of the class that allows two players to play the game to make sure your above functions are working correctly.
2. Some asserts that correspond to a simulated Tic Tac Toe game. These asserts are certainly not exhaustive -- you'll definitely need to write more asserts to properly test your code.
   > _Hint:_ you might want to write a test to check that `game_over` correctly returns `True` when the board is full.

When you're done, push your `a4.py` and `a4_writeup.md` to github.


