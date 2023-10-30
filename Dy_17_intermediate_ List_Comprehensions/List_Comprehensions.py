class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True

    def show_tasks(self, completed=False):
        tasks_to_show = [task for task in self.tasks if task["completed"] == completed]
        for index, task in enumerate(tasks_to_show):
            print(f"{index + 1}. {task['task']}")

    def clear_completed_tasks(self):
        self.tasks = [task for task in self.tasks if not task["completed"]]


def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Complete Task")
        print("4. Show Tasks")
        print("5. Show Completed Tasks")
        print("6. Show Uncompleted Tasks")
        print("7. Clear Completed Tasks")
        print("8. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Enter the task index to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == "3":
            index = int(input("Enter the task index to complete: ")) - 1
            todo_list.complete_task(index)
        elif choice == "4":
            print("\nAll Tasks:")
            todo_list.show_tasks()
        elif choice == "5":
            print("\nCompleted Tasks:")
            todo_list.show_tasks(completed=True)
        elif choice == "6":
            print("\nUncompleted Tasks:")
            todo_list.show_tasks(completed=False)
        elif choice == "7":
            todo_list.clear_completed_tasks()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
