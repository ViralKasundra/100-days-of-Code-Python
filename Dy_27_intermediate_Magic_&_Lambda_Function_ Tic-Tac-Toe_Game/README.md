**Tic-Tac-Toe Game**

**Introduction**

The Tic-Tac-Toe game is a classic two-player game where players take turns to mark spaces in a 3x3 grid. The goal is to have three of your symbols (either "X" or "O") in a row, column, or diagonal. This document outlines the requirements and technical details for the development of the Tic-Tac-Toe game.

**Functional Requirements**

The game must provide a 3x3 grid for players to make their moves.

Players should take turns to click on an empty space in the grid to mark it with their symbol.

The game should determine a win when a player has three of their symbols in a row, column, or diagonal.

If all spaces are filled and no win is detected, the game is declared a tie.

A "Play Again" button should be displayed after the game is finished (win or tie) to allow players to start a new game.

The game must display messages for win and tie situations.
**
Non-Functional Requirements**

The game should be implemented in Python using the Tkinter library for the graphical user interface.

The frame size of the game should be increased for better visibility.

The buttons in the grid should be appropriately sized for easy interaction.

Python magic methods should be used for specific tasks.

Python lambda functions should be used for button commands and other functional components.

****Technical Details****

**Python Magic Methods**

Python magic methods, also known as dunder methods (e.g., __init__, __str__, etc.), are used for object initialization and customization.

In the Tic-Tac-Toe game, these methods are used to set up the game, initialize the board, and handle various tasks.

**Python Lambda Functions**

Lambda functions are used in the game for button commands. They are particularly used to pass the button object to the make_move function, allowing for dynamic button interaction. Lambda functions make it easier to bind the buttons to the correct actions.

**Code Structure**

The code is organized into a main class, TicTacToe, which manages the game logic and user interface.

A CustomButton class is used to create buttons with specific attributes.

The game is played in a 3x3 grid, and a "Play Again" button is available for restarting the game.

Messages are displayed on a label to inform players of game outcomes.
