# main.py

from decorators import access_required, load_library_data, save_library_data

user_level = "user"  # Default user level is librarian

def list_books(user_level):
    books = load_library_data()
    if user_level in access_levels:
        if user_level == "user":
            return "\n".join([f"Title: {book['title']}, Author: {book['author']}" for book in books])
        elif user_level == "librarian" or user_level == "admin":
            return "\n".join([f"Title: {book['title']}, Author: {book['author']}, Copies: {book['copies']}" for book in books])
    return "Access Denied"

@access_required("user")
def checkout_book(user_access_level, title):
    books = load_library_data()
    for book in books:
        if book["title"] == title:
            if book["copies"] > 0:
                book["copies"] -= 1
                save_library_data(books)
                return f"Checked out book: {title}"
            else:
                return f"No copies available for book: {title}"
    return f"Book not found: {title}"

def main_menu():
    print("Library Access Control System")
    print("1. List Books")
    print("2. Checkout Book")
    print("3. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        print(list_books(user_level))
    elif choice == "2":
        title = input("Enter the title of the book to check out: ")
        print(checkout_book(user_level, title))  # Ensure 'title' is passed as an argument
    elif choice == "3":
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    while True:
        main_menu()
