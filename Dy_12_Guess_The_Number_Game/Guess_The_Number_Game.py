import random

def guess_the_number():
    print("Welcome to Guess the Number Game!")
    play_again = "yes"

    while play_again.lower() == "yes":
        secret_number = random.randint(1, 100)
        attempts = 0
        max_attempts = 10

        print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts to guess it.")

        while attempts < max_attempts:
            try:
                guess = int(input("Guess the number: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
                break

        if attempts >= max_attempts:
            print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")

        play_again = input("Do you want to play again? (yes/no): ")

if __name__ == "__main__":
    guess_the_number()
