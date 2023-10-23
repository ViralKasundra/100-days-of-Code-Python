# Python Sets Application (Complex)

# Initialize an empty set
my_set = set()

# Function to add elements to a set
def add_to_set():
    element = input("Enter an element to add to the set: ")
    my_set.add(element)
    print(f"'{element}' added to the set.")

# Function to remove elements from a set
def remove_from_set():
    element = input("Enter an element to remove from the set: ")
    if element in my_set:
        my_set.remove(element)
        print(f"'{element}' removed from the set.")
    else:
        print(f"'{element}' not found in the set.")

# Function to demonstrate immutable sets
def immutable_sets():
    try:
        my_set[0] = 'x'  # This will raise a TypeError
    except TypeError as e:
        print("Immutable Sets Exception:", e)

# Function to perform set comprehensions
def set_comprehensions():
    numbers = {x for x in range(10)}
    print("Set of Numbers (0-9):", numbers)

# Function to demonstrate set intersection
def set_intersection():
    another_set = set(input("Enter a comma-separated set of elements to find the intersection: ").split(","))
    common_elements = my_set.intersection(another_set)
    print("Intersection of Sets:", common_elements)

# Function to update the set
def update_set():
    elements = input("Enter a comma-separated set of elements to update the set: ").split(",")
    my_set.update(elements)
    print("Set Updated:", my_set)

# Function to copy the set
def copy_set():
    new_set = my_set.copy()
    print("Copy of the Set:", new_set)

# Function to clear the set
def clear_set():
    my_set.clear()
    print("Set Cleared. It's now an empty set.")

# Function to convert the set
def convert_set():
    list_from_set = list(my_set)
    tuple_from_set = tuple(my_set)
    print("Set converted to List:", list_from_set)
    print("Set converted to Tuple:", tuple_from_set)

# Function to check set equality and subsets
def check_equality_and_subsets():
    other_set = set(input("Enter a comma-separated set of elements to compare: ").split(","))
    is_equal = my_set == other_set
    is_subset = my_set.issubset(other_set)
    print("Set Equality:", is_equal)
    print("Set is a Subset:", is_subset)

# Main application loop
while True:
    print("\nPython Sets Application (Complex)")
    print("1. Add to Set")
    print("2. Remove from Set")
    print("3. Immutable Sets Exception")
    print("4. Set Comprehensions")
    print("5. Set Intersection")
    print("6. Update Set")
    print("7. Copy Set")
    print("8. Clear Set")
    print("9. Convert Set")
    print("10. Check Equality and Subsets")
    print("11. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6/7/8/9/10/11): ")

    if choice == '1':
        add_to_set()
    elif choice == '2':
        remove_from_set()
    elif choice == '3':
        immutable_sets()
    elif choice == '4':
        set_comprehensions()
    elif choice == '5':
        set_intersection()
    elif choice == '6':
        update_set()
    elif choice == '7':
        copy_set()
    elif choice == '8':
        clear_set()
    elif choice == '9':
        convert_set()
    elif choice == '10':
        check_equality_and_subsets()
    elif choice == '11':
        print("Exiting the Python Sets Application. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option (1/2/3/4/5/6/7/8/9/10/11).")
