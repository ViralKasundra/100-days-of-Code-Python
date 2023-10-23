# Contact Management System using Python Sets

# Initialize a set with sample contacts
contacts = {
    "Alice": {"phone": "123-456-7890", "address": "123 Main St", "pincode": "12345"},
    "Bob": {"phone": "456-789-0123", "address": "456 Elm St", "pincode": "45678"},
    "Charlie": {"phone": "789-012-3456", "address": "789 Oak St", "pincode": "78901"},
    "David": {"phone": "234-567-8901", "address": "234 Maple St", "pincode": "23456"},
    "Eve": {"phone": "567-890-1234", "address": "567 Pine St", "pincode": "56789"}
}

# Function to add a contact to the set
def add_contact():
    name = input("Enter the name of the contact: ")
    phone = input("Enter the phone number: ")
    address = input("Enter the address: ")
    pincode = input("Enter the pin code: ")

    if name not in contacts:
        contacts[name] = {"phone": phone, "address": address, "pincode": pincode}
        print(f"Contact '{name}' added successfully.")
    else:
        print(f"Contact '{name}' already exists in the set.")

# Function to remove a contact from the set
def remove_contact():
    name = input("Enter the name of the contact to remove: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' removed from the set.")
    else:
        print(f"Contact '{name}' not found in the set.")

# Function to update a contact in the set
def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input("Enter the new phone number: ")
        address = input("Enter the new address: ")
        pincode = input("Enter the new pin code: ")
        contacts[name] = {"phone": phone, "address": address, "pincode": pincode}
        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"Contact '{name}' not found in the set.")

# Function to display all contacts in the set
def display_contacts():
    if not contacts:
        print("No contacts in the set.")
    else:
        print("List of Contacts:")
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Address: {info['address']}")
            print(f"Pincode: {info['pincode']}")
            print()

# Function to find common contacts between two sets
def find_common_contacts():
    other_contacts = set(input("Enter comma-separated contacts to find common contacts: ").split(","))
    common = contacts.keys() & other_contacts
    if common:
        print("Common Contacts:", common)
    else:
        print("No common contacts found.")

# Main application loop
while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Update Contact")
    print("4. Display Contacts")
    print("5. Find Common Contacts")
    print("6. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        remove_contact()
    elif choice == '3':
        update_contact()
    elif choice == '4':
        display_contacts()
    elif choice == '5':
        find_common_contacts()
    elif choice == '6':
        print("Exiting the Contact Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4/5/6).")
