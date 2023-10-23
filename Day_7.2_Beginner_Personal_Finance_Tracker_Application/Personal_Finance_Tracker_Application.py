# Python Exceptions Application

import traceback
import sys

# List to store the history of exceptions
exception_history = []

# Dictionary to store information about common exceptions
common_exceptions = {
    'ZeroDivisionError': 'Occurs when dividing by zero.',
    'ValueError': 'Occurs when an invalid value is provided to a function.',
    'TypeError': 'Occurs when an operation is performed on an inappropriate data type.',
    'FileNotFoundError': 'Occurs when attempting to access a file that does not exist.',
    # Add more common exceptions and descriptions as needed
}

# Function to handle common exceptions
def handle_common_exceptions():
    while True:
        print("Common Exceptions:")
        for index, exception in enumerate(common_exceptions, start=1):
            print(f"{index}. {exception}")

        choice = input("Select an exception (1/2/3/4/... or 'q' to quit): ")
        if choice == 'q':
            break
        try:
            index = int(choice) - 1
            selected_exception = list(common_exceptions.keys())[index]
            raise_exception(selected_exception)
        except (ValueError, IndexError):
            print("Invalid choice. Please select a valid option or 'q' to quit.")

# Function to raise a specific exception
def raise_exception(exception_name):
    try:
        if exception_name == 'ZeroDivisionError':
            result = 1 / 0
        elif exception_name == 'ValueError':
            value = int("invalid")
        elif exception_name == 'TypeError':
            value = "string" + 1
        elif exception_name == 'FileNotFoundError':
            with open("non_existent_file.txt", "r") as file:
                file.read()
        # Add handling for additional common exceptions here
    except Exception as e:
        record_exception(e)
        print(f"Exception: {exception_name}")
        print(f"Description: {common_exceptions[exception_name]}")
        print(f"Message: {str(e)}")

# Function to practice advanced exception handling
def practice_advanced_exception_handling():
    try:
        num = int(input("Enter a number: "))
        result = 10 / num
        print(f"Result: {result}")
    except ZeroDivisionError as e:
        record_exception(e)
        print("Error: Division by zero is not allowed.")
    except ValueError as e:
        record_exception(e)
        print("Error: Invalid input. Please enter a valid number.")
    except Exception as e:
        record_exception(e)
        print(f"An unexpected error occurred: {str(e)}")

# Function to define and raise a custom exception
class CustomException(Exception):
    pass

def define_and_raise_custom_exception():
    try:
        raise CustomException("This is a custom exception.")
    except CustomException as e:
        record_exception(e)
        print(f"Custom Exception Raised: {str(e)}")

# Function to view the exception history
def view_exception_history():
    if not exception_history:
        print("No exceptions in the history.")
    else:
        print("Exception History:")
        for index, exception in enumerate(exception_history, start=1):
            print(f"{index}. {exception}")

# Function to save the exception history to a file
def save_exception_history_to_file():
    if not exception_history:
        print("No exceptions to save. Exception history is empty.")
    else:
        filename = input("Enter the filename to save the exception history: ")
        try:
            with open(filename, 'w') as file:
                file.write("\n".join(exception_history))
            print(f"Exception history saved to {filename}.")
        except Exception as e:
            print(f"Error while saving the exception history: {str(e)}")

# Function to catch unhandled exceptions globally
def global_exception_handler(exctype, value, tb):
    formatted_traceback = traceback.format_exception(exctype, value, tb)
    exception_message = "".join(formatted_traceback)
    record_exception(exception_message)
    print("An unhandled exception occurred:")
    print(exception_message)

# Function to record exceptions in the history
def record_exception(exception):
    exception_history.append(str(exception))

# Set the global exception handler
sys.excepthook = global_exception_handler

# Main application loop
while True:
    print("\nPython Exceptions Application")
    print("1. Handle Common Exceptions")
    print("2. Practice Advanced Exception Handling")
    print("3. Define and Raise Custom Exceptions")
    print("4. View Exception History")
    print("5. Save Exception History to File")
    print("6. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == '1':
        handle_common_exceptions()
    elif choice == '2':
        practice_advanced_exception_handling()
    elif choice == '3':
        define_and_raise_custom_exception()
    elif choice == '4':
        view_exception_history()
    elif choice == '5':
        save_exception_history_to_file()
    elif choice == '6':
        print("Exiting the Python Exceptions Application. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4/5/6).")
