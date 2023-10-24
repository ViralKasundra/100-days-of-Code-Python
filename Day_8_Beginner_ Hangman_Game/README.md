******Overview******

The Hangman Game is a Python-based word guessing game in which players attempt to guess a hidden word by suggesting letters one at a time. The game provides ASCII art representation of a hangman figure as players make incorrect guesses. The game continues until the player either guesses the word or runs out of attempts.

****Features****

**1. Select Random Word**
The game randomly selects a word from a predefined list.
Input: None.
Output: A word is chosen for the game.

**2. Display Hangman Art**
The game displays ASCII art representing the hangman figure.
Input: The number of incorrect attempts.
Output: The appropriate hangman figure is shown.

**3. Guess a Letter**
The player can guess a letter in an attempt to guess the hidden word.
Input: A single letter.
Output: The game provides feedback on the correctness of the guess and updates the word display.

**4. Word Display**
The game displays the word with underscores for unrevealed letters and reveals correct guesses.
Input: None.
Output: The current state of the word, including guessed letters.

**5. Guessed Letters**
The game maintains a list of guessed letters.
Input: None.
Output: The list of guessed letters is displayed.

**6. Win Condition**
The game checks if the player has guessed the word correctly.
Input: None.
Output: A message is displayed if the player wins the game.

**7. Lose Condition**
The game checks if the player has exhausted their allowed attempts.
Input: None.
Output: A message is displayed if the player loses the game.

**8. Validate Input**
The game validates user input to ensure it is a single letter.
Input: User input.
Output: Feedback is provided for invalid input.

**Assumptions and Constraints**
1.The game uses a predefined list of words.
2.The hangman figure consists of seven stages.
3.Players have a limited number of attempts (6 in this case).
4.The game accepts single-letter guesses from the player.
5.Only one letter can be guessed at a time.
6.The game does not consider letter case (case-insensitive).
