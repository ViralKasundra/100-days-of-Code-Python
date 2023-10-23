import random

# Define character sets for generating passwords
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'

def generate_password(nr_letters, nr_symbols, nr_numbers):
    # Check if the input parameters are valid
    if nr_letters < 1 or nr_symbols < 1 or nr_numbers < 1:
        return "Invalid parameters. Please select at least one character of each type."

    # Combine character sets for password generation
    all_characters = letters + symbols + numbers

    # Generate the password by randomly choosing characters from the combined set
    password = [random.choice(all_characters) for _ in range(nr_letters + nr_symbols + nr_numbers)]

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    # Convert the list of characters into a string and return the password
    return ''.join(password)

def main():
    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))

    generated_password = generate_password(nr_letters, nr_symbols, nr_numbers)
    print("Your generated password is:")
    print(generated_password)

if __name__ == "__main__":
    main()
