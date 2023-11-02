import json
from decorators import authenticate, admin_required

# Load user and task data
def load_user_data():
    try:
        with open('user_data.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def load_task_data():
    try:
        with open('task_data.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_user_data(data):
    with open('user_data.json', 'w') as file:
        json.dump(data, file, indent=4)

def save_task_data(data):
    with open('task_data.json', 'w') as file:
        json.dump(data, file, indent=4)

# User management
def create_account():
    users = load_user_data()
    username = input("Enter a username: ")
    if username in users:
        print("Username already exists.")
        return

    password = input("Enter a password: ")
    users[username] = {'password': password, 'role': 'user'}
    save_user_data(users)
    print("Account created successfully.")

@authenticate
def login(username):
    print(f"Welcome, {username}!")

# Task management
def add_task(username):
    tasks = load_task_data()
    title = input("Enter task title: ")
    tasks.append({'username': username, 'title': title, 'completed': False})
    save_task_data(tasks)
    print("Task added successfully.")

@authenticate
def view_tasks(username):
    tasks = load_task_data()
    user_tasks = [task for task in tasks if task['username'] == username]
    print("Your tasks:")
    for i, task in enumerate(user_tasks, start=1):
        print(f"{i}. [{task['completed']}] {task['title']}")

@admin_required
def delete_task():
    tasks = load_task_data()
    task_index = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        del tasks[task_index]
        save_task_data(tasks)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

if __name__ == '__main__':
    while True:
        print("\nTask Management System")
        print("1. Create Account")
        print("2. Login")
        print("3. Add Task")
        print("4. View Tasks")
        print("5. Delete Task (Admin)")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if username in load_user_data() and load_user_data()[username]['password'] == password:
                login(username)
                while True:
                    print("\nTask Management System")
                    print("3. Add Task")
                    print("4. View Tasks")
                    print("5. Delete Task (Admin)")
                    print("6. Logout")

                    inner_choice = input("Select an option: ")

                    if inner_choice == '3':
                        username = input("Enter your username: ")
                        add_task(username)
                    elif inner_choice == '4':
                        username = input("Enter your username: ")
                        view_tasks(username)
                    elif inner_choice == '5':
                        delete_task(username)

                    elif inner_choice == '6':
                        print("Logged out.")
                        break
                    else:
                        print("Invalid choice. Please select a valid option.")
            else:
                print("Login failed. Please check your credentials.")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

