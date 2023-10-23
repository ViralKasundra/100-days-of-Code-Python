# Library Catalog Management Application

from datetime import datetime, timedelta

# Initialize the library catalog (dictionary) with some initial books
library_catalog = {
    "Book 1": {
        "Author": "Author A",
        "Genre": "Fiction",
        "Year": "2020",
        "Copies Available": 3,
        "Total Copies": 3,
    },
    "Book 2": {
        "Author": "Author B",
        "Genre": "Mystery",
        "Year": "2019",
        "Copies Available": 2,
        "Total Copies": 2,
    },
    "Book 3": {
        "Author": "Author C",
        "Genre": "Non-fiction",
        "Year": "2021",
        "Copies Available": 1,
        "Total Copies": 1,
    },
}

# Initialize the borrowed books dictionary
borrowed_books = {
    "Book 4": "2023-10-15",
}


# Function to add a book to the library catalog
def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author's name: ")
    genre = input("Enter the genre: ")
    year = input("Enter the publication year: ")
    copies = int(input("Enter the number of copies available: "))

    if title not in library_catalog:
        book_details = {
            "Author": author,
            "Genre": genre,
            "Year": year,
            "Copies Available": copies,
            "Total Copies": copies,
        }
        library_catalog[title] = book_details
        print(f"Book '{title}' added to the library catalog.")
    else:
        print(f"Book '{title}' already exists in the catalog.")


# Function to update book details in the library catalog
def update_book():
    title = input("Enter the title of the book to update: ")
    if title in library_catalog:
        print("Select the detail to update:")
        print("1. Author")
        print("2. Genre")
        print("3. Publication Year")
        print("4. Number of Copies")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            author = input("Enter the new author's name: ")
            library_catalog[title]["Author"] = author
        elif choice == '2':
            genre = input("Enter the new genre: ")
            library_catalog[title]["Genre"] = genre
        elif choice == '3':
            year = input("Enter the new publication year: ")
            library_catalog[title]["Year"] = year
        elif choice == '4':
            copies = int(input("Enter the new number of copies available: "))
            library_catalog[title]["Copies Available"] = copies
            library_catalog[title]["Total Copies"] = copies
        else:
            print("Invalid choice.")
        print(f"Book '{title}' details updated successfully.")
    else:
        print(f"Book '{title}' not found in the catalog.")


# Function to borrow a book
def borrow_book():
    title = input("Enter the title of the book to borrow: ")
    if title in library_catalog:
        if library_catalog[title]["Copies Available"] > 0:
            if title not in borrowed_books:
                due_date = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
                borrowed_books[title] = due_date
                library_catalog[title]["Copies Available"] -= 1
                print(f"Book '{title}' borrowed successfully. Due date: {due_date}")
            else:
                print(f"Book '{title}' is already borrowed. Due date: {borrowed_books[title]}")
        else:
            print(f"No copies of '{title}' are available for borrowing.")
    else:
        print(f"Book '{title}' not found in the catalog.")


# Function to return a borrowed book
def return_book():
    title = input("Enter the title of the book to return: ")
    if title in borrowed_books:
        due_date = borrowed_books[title]
        return_date = input(f"Enter the return date (yyyy-mm-dd) for '{title}' (due date: {due_date}): ")
        if return_date <= due_date:
            library_catalog[title]["Copies Available"] += 1
            del borrowed_books[title]
            print(f"Book '{title}' returned successfully.")
        else:
            print(f"Book '{title}' is overdue. Return not allowed.")
    else:
        print(f"Book '{title}' is not in the list of borrowed books.")


# Function to search for books in the library catalog
def search_books():
    search_term = input("Enter a title, author, or genre to search for books: ")
    found_books = []

    for title, details in library_catalog.items():
        if (search_term.lower() in title.lower()) or (search_term.lower() in details["Author"].lower()) or (
                search_term.lower() in details["Genre"].lower()):
            found_books.append((title, details))

    if found_books:
        print("Matching Books:")
        for book in found_books:
            print(f"Title: {book[0]}")
            print(f"Author: {book[1]['Author']}")
            print(f"Genre: {book[1]['Genre']}")
            print(f"Publication Year: {book[1]['Year']}")
            print(f"Copies Available: {book[1]['Copies Available']} / Total Copies: {book[1]['Total Copies']}")
            print()
    else:
        print("No matching books found in the catalog.")


# Function to generate a report of books in the library catalog
def generate_report():
    print("Library Catalog Report:")
    for title, details in library_catalog.items():
        print(f"Title: {title}")
        print(f"Author: {details['Author']}")
        print(f"Genre: {details['Genre']}")
        print(f"Publication Year: {details['Year']}")
        print(f"Copies Available: {details['Copies Available']} / Total Copies: {details['Total Copies']}")
        print()


# Function to view borrowed books
def view_borrowed_books():
    if borrowed_books:
        print("Borrowed Books:")
        for title, due_date in borrowed_books.items():
            print(f"Title: {title}, Due Date: {due_date}")
    else:
        print("No books have been borrowed.")


# ... (other functions remain unchanged)

# Main application loop
while True:
    print("\nLibrary Catalog Management Application")
    print("1. Add Book")
    print("2. Update Book Details")
    print("3. Search for Books")
    print("4. Generate Catalog Report")
    print("5. Borrow a Book")
    print("6. Return a Borrowed Book")
    print("7. View Borrowed Books")
    print("8. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")

    if choice == '1':
        add_book()
    elif choice == '2':
        update_book()
    elif choice == '3':
        search_books()
    elif choice == '4':
        generate_report()
    elif choice == '5':
        borrow_book()
    elif choice == '6':
        return_book()
    elif choice == '7':
        view_borrowed_books()
    elif choice == '8':
        print("Exiting the Library Catalog Management Application. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4/5/6/7/8).")
