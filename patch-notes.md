# To-Dos
- Prompt at the end of the game to start a new game with the same players and marks right away
- Let players choose their marks
- Actual coin toss as option for who will start the game - has to include selection of head or tails for one player.
- Set default names if no input is given for player names
- Improve error message for taken spot
- Create a visual interface

# Version history

## Version 0.3 - 2023/08/22
- Rework of README. Now includes "How to start the game", "Rules" and "Support"
- Added selection for a randomizer for the starting player
- Fixed errors for invalid inputs (string or floats) when setting your mark

## Version 0.2 - 2023/08/21
Changes:
- Display an error message when a spot is already taken or spot selected is out of bounds and trigger re-select by active player

## Version 0.1 - 2023/08/18
The very first release! With this you are able to play a very simple and straightforward game of Tic-Tac-Toe against a friend (or yourself, there is nothing wrong with being your own best friend =)<br>
Functionality includes:
- Give names to Player 1 ('O' mark) and Player 2 ('X' mark)
- Alternate setting your marks with Player 1 starting on a 3x3 matrix by choosing fields 1-9
- A maximum of 9 turns, after which a draw will be called
- If any player manages to get 3 marks in a row, a win message will be displayed