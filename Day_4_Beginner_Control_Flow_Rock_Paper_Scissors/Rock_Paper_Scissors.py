import random

# Define the three hand gestures as string variables
rock = '''   
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''   
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''   
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Create a list containing the three hand gestures
choices = [rock, paper, scissors]

def get_user_choice():
    while True:
        try:
            user_choice = int(input(
                "What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
            if 0 <= user_choice <= 2:
                return user_choice
            else:
                print("Invalid input. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number (0, 1, or 2).")

def main():
    # Get the user's choice and print the corresponding gesture
    user_choice = get_user_choice()
    print("You chose:\n", choices[user_choice])

    # Generate a random choice for the computer and print the corresponding gesture
    comp_choice = random.randint(0, 2)
    print("Computer chose:\n", choices[comp_choice])

    # Compare the user's choice with the computer's choice and print the result
    if user_choice == comp_choice:
        print("Match draw...")
    elif (user_choice == 0 and comp_choice == 2) or (user_choice == 1 and comp_choice == 0) or (user_choice == 2 and comp_choice == 1):
        print("You Win! 😄")
    else:
        print("You Lose ☹️")

if __name__ == "__main__":
    main()
