# Python Dictionaries Operation Application

# Initialize an empty dictionary
my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "email": "john@example.com"
}

# Function to add key-value pairs to the dictionary
def add_to_dictionary():
    key = input("Enter a key: ")
    value = input("Enter a value: ")
    my_dict[key] = value
    print(f"Key-Value pair '{key}': '{value}' added to the dictionary.")

# Function to access values using keys
def access_dictionary():
    key = input("Enter a key to access its value: ")
    if key in my_dict:
        value = my_dict[key]
        print(f"The value for key '{key}' is '{value}'.")
    else:
        print(f"Key '{key}' not found in the dictionary.")

# Function to modify values in the dictionary
def modify_dictionary():
    key = input("Enter a key to modify its value: ")
    if key in my_dict:
        value = input(f"Enter the new value for key '{key}': ")
        my_dict[key] = value
        print(f"Value for key '{key}' updated to '{value}'.")
    else:
        print(f"Key '{key}' not found in the dictionary.")

# Function to delete key-value pairs from the dictionary
def delete_from_dictionary():
    key = input("Enter a key to delete: ")
    if key in my_dict:
        del my_dict[key]
        print(f"Key-Value pair '{key}': '{my_dict[key]}' deleted from the dictionary.")
    else:
        print(f"Key '{key}' not found in the dictionary.")

# Function to demonstrate nested dictionaries
def nested_dictionaries():
    nested_dict = {}
    key = input("Enter a key for the nested dictionary: ")
    nested_key = input("Enter a key for the nested value: ")
    nested_value = input("Enter a value for the nested key: ")
    nested_dict[nested_key] = nested_value
    my_dict[key] = nested_dict
    print(f"Nested dictionary added under key '{key}'.")

# Function to use the dictionary method get
def dictionary_get():
    key = input("Enter a key to access its value using 'get': ")
    value = my_dict.get(key, "Key not found")
    print(f"The value for key '{key}' (using 'get') is '{value}'.")

# Function to display dictionary keys
def display_keys():
    keys = my_dict.keys()
    print("Keys in the dictionary:", list(keys))

# Function to display dictionary values
def display_values():
    values = my_dict.values()
    print("Values in the dictionary:", list(values))

# Function to display dictionary items
def display_items():
    items = my_dict.items()
    print("Key-Value pairs in the dictionary:", list(items))

# Function to demonstrate looping through dictionaries
def loop_through_dictionary():
    print("Looping through the dictionary:")
    for key, value in my_dict.items():
        print(f"Key: '{key}', Value: '{value}'")

# Function to create a dictionary with default values
def default_value_dictionary():
    from collections import defaultdict
    default_dict = defaultdict(int)
    print("Default dictionary created with default integer values.")
    print("Sample usage: default_dict['key'] will return 0 if the key doesn't exist.")

# Main application loop
while True:
    print("\nPython Dictionaries Operation Application")
    print("1. Add to Dictionary")
    print("2. Access Dictionary")
    print("3. Modify Dictionary")
    print("4. Delete from Dictionary")
    print("5. Nested Dictionaries")
    print("6. Dictionary Method - Get")
    print("7. Dictionary Method - Keys")
    print("8. Dictionary Method - Values")
    print("9. Dictionary Method - Items")
    print("10. Loop Through Dictionary")
    print("11. Dictionary with Default Values")
    print("12. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6/7/8/9/10/11/12): ")

    if choice == '1':
        add_to_dictionary()
    elif choice == '2':
        access_dictionary()
    elif choice == '3':
        modify_dictionary()
    elif choice == '4':
        delete_from_dictionary()
    elif choice == '5':
        nested_dictionaries()
    elif choice == '6':
        dictionary_get()
    elif choice == '7':
        display_keys()
    elif choice == '8':
        display_values()
    elif choice == '9':
        display_items()
    elif choice == '10':
        loop_through_dictionary()
    elif choice == '11':
        default_value_dictionary()
    elif choice == '12':
        print("Exiting the Python Dictionaries Operation Application. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4/5/6/7/8/9/10/11/12).")
