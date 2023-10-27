import json

class Book:
    def __init__(self, title, author, ISBN, checked_out):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.checked_out = checked_out

    def check_out(self):
        if not self.checked_out:
            self.checked_out = True
            print(f"{self.title} by {self.author} has been checked out.")
            return True
        else:
            print(f"{self.title} is already checked out.")
            return False

    def check_in(self):
        if self.checked_out:
            self.checked_out = False
            print(f"{self.title} has been checked in.")
            return True
        else:
            print(f"{self.title} is already checked in.")
            return False

class Patron:
    def __init__(self, name, patron_id, books_checked_out):
        self.name = name
        self.patron_id = patron_id
        self.books_checked_out = books_checked_out

    def check_out_book(self, book):
        if len(self.books_checked_out) < 3:
            if not book.checked_out:
                if book.check_out():
                    self.books_checked_out.append(book.title)
                    return True
                else:
                    return False
            else:
                print(f"Sorry, {book.title} is already checked out.")
                return False
        else:
            print(f"Sorry, you have reached the maximum limit of checked-out books.")
            return False

    def return_book(self, book):
        if book.title in self.books_checked_out:
            if book.check_in():
                self.books_checked_out.remove(book.title)
                return True
            else:
                return False
        else:
            print(f"You can't return {book.title} because it's not in your checked-out books.")
            return False

class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)

    def add_patron(self, patron):
        self.patrons.append(patron)

    def register_patron(self):
        name = input("Enter the name of the new patron: ")
        patron_id = len(self.patrons) + 1
        new_patron = Patron(name, patron_id, [])
        self.patrons.append(new_patron)
        print(f"New patron '{name}' has been registered with patron ID {patron_id}.")

    def save_data(self):
        with open('book_data.json', 'w') as book_file:
            json.dump([vars(book) for book in self.books], book_file, indent=4)
        with open('patron_data.json', 'w') as patron_file:
            json.dump([vars(patron) for patron in self.patrons], patron_file, indent=4)

    def load_data(self):
        try:
            with open('book_data.json', 'r') as book_file:
                book_data = json.load(book_file)
                self.books = [Book(**data) for data in book_data]
        except FileNotFoundError:
            self.books = []

        try:
            with open('patron_data.json', 'r') as patron_file:
                patron_data = json.load(patron_file)
                self.patrons = [Patron(**data) for data in patron_data]
        except FileNotFoundError:
            self.patrons = []

# Create a library and load data from JSON files
library = Library()
library.load_data()

# Main interactive loop
while True:
    print("\nLibrary Operations:")
    print("1. Check Out a Book")
    print("2. Return a Book")
    print("3. Register a New Patron")
    print("4. Save and Exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        patron_name = input("Enter your patron name: ")
        book_title = input("Enter the title of the book you want to check out: ")

        patron = next((p for p in library.patrons if p.name == patron_name), None)
        book = next((b for b in library.books if b.title == book_title), None)

        if patron and book:
            if patron.check_out_book(book):
                library.save_data()
        else:
            print("Patron or book not found or the book is already checked out.")

    elif choice == "2":
        patron_name = input("Enter your patron name: ")
        book_title = input("Enter the title of the book you want to return: ")

        patron = next((p for p in library.patrons if p.name == patron_name), None)
        book = next((b for b in library.books if b.title == book_title), None)

        if patron and book:
            if patron.return_book(book):
                library.save_data()
        else:
            print("Patron or book not found.")

    elif choice == "3":
        # Check if the patron already exists before registering a new one
        patron_name = input("Enter the name of the new patron: ")
        if not any(p.name == patron_name for p in library.patrons):
            library.register_patron()
            library.save_data()
        else:
            print(f"A patron with the name '{patron_name}' already exists.")

    elif choice == "4":
        print("Saving data and exiting...")
        library.save_data()
        break

    else:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")
