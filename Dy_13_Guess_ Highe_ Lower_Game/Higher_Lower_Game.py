import random
from pyfiglet import Figlet

# Define a list of celebrities with their Instagram follower counts
celebrities = [
    {"name": "Selena Gomez", "followers": 255_000_000},
    {"name": "Dwayne Johnson", "followers": 250_000_000},
    {"name": "Kylie Jenner", "followers": 247_000_000},
    # Add more celebrities here...
]

def get_next_celebrity(previous_celebrity):
    next_celebrity = random.choice(celebrities)
    while next_celebrity == previous_celebrity:
        next_celebrity = random.choice(celebrities)
    return next_celebrity

def print_welcome_message():
    f = Figlet(font='big')
    print(f.renderText('Higher Lower Game'))
    print("Guess whether the next celebrity has more or fewer Instagram followers.")

def higher_lower_game():
    print_welcome_message()
    
    player_name = input("Enter your name: ")
    print(f"Welcome, {player_name}!")
    
    score = 0  # Initialize the player's score
    prev_celebrity = None  # Start without a previous celebrity
    
    while True:
        if prev_celebrity is None:
            prev_celebrity = get_next_celebrity(prev_celebrity)
        
        print(f"Current Celebrity: {prev_celebrity['name']} - {prev_celebrity['followers']} followers")
        print("Is the next celebrity's follower count higher or lower?")
        
        next_celebrity = get_next_celebrity(prev_celebrity)
        
        guess = input("Enter 'higher' or 'lower': ").strip().lower()
        
        if guess in {"higher", "lower"}:
            if (guess == "higher" and next_celebrity["followers"] > prev_celebrity["followers"]) or \
               (guess == "lower" and next_celebrity["followers"] < prev_celebrity["followers"]):
                print("Correct! You guessed it right.")
                score += 1
                prev_celebrity = next_celebrity
            else:
                print(f"Wrong guess, {player_name}! Your final score is {score}.")
                break
        else:
            print("Invalid input. Please enter 'higher' or 'lower'.")

if __name__ == "__main__":
    higher_lower_game()
