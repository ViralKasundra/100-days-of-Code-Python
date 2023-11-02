****Project Overview****

The Interactive Library Access Control System is a Python-based command-line application that simulates a library access control system. This system allows users with different access levels to perform actions such as listing books and checking out books. The system maintains book data in a JSON file, and users can interact with the program through a text-based menu.

****Project Objectives****

The primary objectives of this project are as follows:

**User Access Control:** The system will manage different user access levels, including "user," "librarian," and "admin." Users with higher access levels will have access to more features.

**Book Data Management:** The system will maintain book data, including book titles, authors, and the number of copies available, in a JSON file.

**Menu-Driven Interface:** Users will interact with the program through a simple menu, where they can select actions based on their access level.

**List Books:** Users can list available books, including details such as title, author, and the number of copies (for librarians and admins).

**Checkout Books:** Users can check out books, and the system will update the available copies accordingly.

**Functional Requirements**

**User Access Control**

The system will support three access levels: "user," "librarian," and "admin."

Access levels will determine which features and actions a user can perform within the system.

**Book Data Management**

The system will store book data in a JSON file (library_data.json).

The JSON file will include information about each book, such as title, author, and the number of copies available.

**Menu-Driven Interface**

Upon running the program, users will be presented with a menu with the following options:

List Books

Checkout Book

Exit

**List Books**

Users with "user," "librarian," or "admin" access will be able to list available books.

The list will include details such as title and author.

For librarians and admins, the list will also include the number of copies available for each book.

**Checkout Books**

Users with "user," "librarian," or "admin" access will be able to check out books.

The system will check if the selected book is available (has at least one copy), and if so, it will decrease the available copies by one.

**Non-Functional Requirements**

The system should be user-friendly and provide clear instructions for using the menu.

Book data should be stored and loaded from the JSON file efficiently.

The program should handle user input validation to prevent errors and provide informative error messages.

**Dependencies**
The project requires Python 3.x to run.

No external libraries or packages are used.

**Data Structure**

Book data will be stored in a JSON file (library_data.json) with the following structure for each book:

{
    "title": "Book Title",
    "author": "Author Name",
    "copies": 3
}
