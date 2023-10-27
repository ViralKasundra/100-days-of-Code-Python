**Library Management System Project Requirements**

The goal of this project is to create a basic library management system that allows users to perform the following operations:
Check out a book from the library.
Return a book to the library.
Register a new patron.
Save and load data to/from JSON files for books and patrons.

**Functional Requirements**

**1.Library Operations:**

The system should provide a menu-driven interface for users to select one of the following operations:

Check out a book: Users should be able to check out a book by providing their patron name and the title of the book. The system should handle.

checks for the availability of the book and the patron's eligibility to borrow books.

Return a book:Users should be able to return a book by providing their patron name and the title of the book. The system should handle checks for the patron's ownership of the book 

Register a new patron: Users should be able to register a new patron by providing the patron's name. The system should check if a patron with the same name already exists and only register a new patron if there are no duplicates.

Save and Exit: Users should be able to save data to JSON files and exit the program.

**2.Book Management**:

The system should maintain a list of books with attributes such as title, author, ISBN, and checked-out status.

Books can be checked out and checked in, and their status should be updated accordingly.

**3.Patron Management:**

The system should maintain a list of patrons with attributes such as name, patron ID, and a list of books checked out.

Patrons can check out and return books, and the system should enforce a maximum limit of 3 checked-out books per patron.

**4.Data Persistence:**

The system should save and load data to/from JSON files for both books and patrons.

****Non-Functional Requirements****

**User-Friendly Interface: **

The user interface should be clear and intuitive, providing informative messages and guidance.

**Error Handling:**

The system should handle errors gracefully, providing informative error messages to the user.

Data Integrity: Data in the JSON files should be kept up-to-date and accurate.

Efficiency:The system should efficiently search for books and patrons, ensuring that operations are performed without unnecessary delays.

**Constraints**

The maximum number of books a patron can check out is 3.

Patron names should be unique, and a new patron should not be registered with a name that already exists.

Data should be stored in JSON files for books and patrons.

**Optional Enhancements**
While the requirements above cover the basic functionality of the library management system, you may consider adding additional features such as:

Search and filter options for books and patrons.

Fine calculation for overdue books.

User authentication and access control.

Integration with a database for data storage.

A web-based or desktop graphical user interface (GUI).

These enhancements can make the system more feature-rich and user-friendly, but they are not mandatory for the core functionality. The complexity and scope of the project can be adjusted based on your objectives and requirements.
