import os

# Function to generate a list of files in a directory
def list_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            yield os.path.join(root, file)

# Function to filter files by extension using a generator
def filter_files_by_extension(directory, extension):
    for file in list_files(directory):
        if file.endswith(f".{extension}"):
            yield file

# Function to filter files by size using a generator
def filter_files_by_size(directory, size):
    for file in list_files(directory):
        if os.path.getsize(file) >= size:
            yield file

# Main program loop
def main():
    directory = input("Enter the directory path: ")

    print("1. List all files")
    print("2. List files by extension")
    print("3. List files by size")
    choice = input("Enter your choice: ")

    if choice == "1":
        for file in list_files(directory):
            print(file)
    elif choice == "2":
        extension = input("Enter the file extension (e.g., 'txt'): ")
        for file in filter_files_by_extension(directory, extension):
            print(file)
    elif choice == "3":
        size = int(input("Enter the minimum file size (in bytes): "))
        for file in filter_files_by_size(directory, size):
            print(file)
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
