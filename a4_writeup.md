# Assignment 4 - Writeup

In assignment 4 we created a basic tic tac toe game so that we could learn object oriented programming. Respond to the following questions.

## Reflection Questions

1. What was the most difficult part to tic-tac-toe?
The most difficult part of tic-tac-toe was debugging the has_won() function because you had to check for every single win condition
possible for the game to work properly. Although I was able to do it faster with for loops, it still took some time testing and fixing
assert errors.

2. Explain how you would add a computer player to the game.
I would either make one of the "X" or "O" players automatically play a move randomly or call an API with the current board positions
to return the best move. However, I think it would be cool if I made my own neural network thing that learns how to play the game the
more the game is played.

3. If you add a computer player, explain (doesn't have to be super technical) how you might get the computer player to play the best move every time. *Note - I am not grading this for a correct answer, I just want to know your thoughts on how you might accomplish it.
Like I said in the previous question, I would either call an API or manage my own neural network. The more the game is played, the more
moves it will learn from, almost just like a human.