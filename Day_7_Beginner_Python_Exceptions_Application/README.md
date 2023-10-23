Python Exceptions Application Requirement Document
1. Introduction
The Python Exceptions Application is designed to demonstrate various aspects of exception handling in Python. It provides a menu-driven interface for users to explore common exceptions, practice advanced exception handling, define and raise custom exceptions, view the exception history, and save the exception history to a file.

2. Features
The application includes the following features:

2.1. Handle Common Exceptions
Users can select from a list of common exceptions.
The application will raise the chosen exception and display its description and message.
2.2. Practice Advanced Exception Handling
Users can input a number.
The application will perform a division operation and handle exceptions like ZeroDivisionError and ValueError.
2.3. Define and Raise Custom Exceptions
Users can define and raise a custom exception.
The application will handle and display the custom exception.
2.4. View Exception History
Users can view the history of exceptions that have been raised.
2.5. Save Exception History to File
Users can save the exception history to a user-specified file.
3. Usage
Run the application.
Select an option from the menu (1/2/3/4/5/6).
Follow the prompts for each option.
Explore and understand Python exception handling.
4. Implementation Details
The application is implemented in Python and consists of several functions:

handle_common_exceptions(): Allows the user to select and raise common exceptions.
raise_exception(): Raises a specific exception and provides details.
practice_advanced_exception_handling(): Demonstrates advanced exception handling.
define_and_raise_custom_exception(): Defines and raises a custom exception.
view_exception_history(): Displays the history of raised exceptions.
save_exception_history_to_file(): Saves the exception history to a user-specified file.
global_exception_handler(): Handles unhandled exceptions and records them.
record_exception(): Records exceptions in the exception history.