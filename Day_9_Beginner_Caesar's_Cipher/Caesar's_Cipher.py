import random

# List of words for the game
word_list = ["python", "java", "javascript", "ruby", "csharp", "php", "html", "css", "swift"]

# Function to select a random word from the list
def choose_word(word_list):
    return random.choice(word_list)

# Function to display the hangman ASCII art
def display_hangman(tries):
    # Hangman ASCII art stages
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
          ---
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
          ---
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     
          ---
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     
          ---
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
          ---
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
          ---
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
          ---
        """
    ]
    return stages[tries]

# Function to play the Hangman game
def play_hangman():
    # Select a word to guess
    word_to_guess = choose_word(word_list)
    # Initialize guessed word with underscores
    guessed_word = ["_"] * len(word_to_guess)
    # List to store guessed letters
    guessed_letters = []
    # Number of tries allowed
    tries = 6

    print("Welcome to Hangman!")

    # Main game loop
    while tries > 0:
        print(display_hangman(6 - tries))
        print("Word: " + " ".join(guessed_word))
        print("Guessed letters: " + ", ".join(guessed_letters))

        # Print the input prompt only once
        guess = input("Guess a letter: ").lower()

        # Validate user input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Check if the guessed letter is in the word
        if guess in word_to_guess:
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    guessed_word[i] = guess

            # Check if the word has been completely guessed
            if "".join(guessed_word) == word_to_guess:
                print("Congratulations! You guessed the word: " + word_to_guess)
                break
        else:
            print("Incorrect guess.")
            tries -= 1

    # End of the game
    if tries == 0:
        print(display_hangman(6))
        print("You ran out of tries. The word was: " + word_to_guess)

# Start the game
if __name__ == "__main__":
    play_hangman()
