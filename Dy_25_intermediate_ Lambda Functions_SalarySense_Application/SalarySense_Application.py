import tkinter as tk
from functools import reduce

# Sample data: List of employee dictionaries with name and salary
employees = [
    {"name": "Alice", "salary": 60000},
    {"name": "Bob", "salary": 75000},
    {"name": "Eve", "salary": 50000},
    {"name": "Charlie", "salary": 90000},
    {"name": "David", "salary": 80000},
]

# Create a Tkinter window
window = tk.Tk()
window.title("Data Processing Application")

# Function to update the employee list in the GUI
def update_employee_list(new_list):
    employee_list.delete(0, tk.END)
    for emp in new_list:
        if isinstance(emp, dict):
            employee_list.insert(tk.END, f"{emp['name']}: ${emp['salary']}")
        else:
            employee_list.insert(tk.END, emp)

# Function to perform map operation on employees
def map_employees(map_func):
    new_employees = list(map(map_func, employees))
    update_employee_list(new_employees)

# Function to perform filter operation on employees
def filter_employees(filter_func):
    filtered_employees = list(filter(filter_func, employees))
    update_employee_list(filtered_employees)

# Function to perform reduce operation on employees
def reduce_employees(reduce_func):
    reduced_salary = reduce(reduce_func, [emp['salary'] for emp in employees])
    result_label.config(text=f"Total Salary: ${reduced_salary:.2f}")

# Function to add a bonus to salaries with input validation
def add_bonus():
    bonus_value = bonus_entry.get()
    try:
        bonus = float(bonus_value)
        map_employees(lambda emp: {"name": emp["name"], "salary": emp["salary"] + bonus})
        error_label.config(text="")  # Clear the error message
    except ValueError:
        error_label.config(text="Invalid bonus value. Please enter a numeric value.")

# Create and display the employee list
employee_list = tk.Listbox(window, width=30, height=10)
employee_list.grid(row=0, column=0, columnspan=2)
update_employee_list(employees)

# Add Bonus
bonus_label = tk.Label(window, text="Add Bonus: $")
bonus_label.grid(row=1, column=0)
bonus_entry = tk.Entry(window)
bonus_entry.grid(row=1, column=1)
bonus_button = tk.Button(window, text="Add Bonus", command=add_bonus)
bonus_button.grid(row=1, column=2)

# Error Label for displaying error messages
error_label = tk.Label(window, text="", fg="red")
error_label.grid(row=2, column=0, columnspan=3)

# Filter High Salary Employees
salary_threshold_label = tk.Label(window, text="Minimum Salary: $")
salary_threshold_label.grid(row=3, column=0)
salary_threshold_entry = tk.Entry(window)
salary_threshold_entry.grid(row=3, column=1)
filter_button = tk.Button(window, text="Filter High Salary", command=lambda: filter_employees(lambda emp: emp["salary"] > float(salary_threshold_entry.get())))
filter_button.grid(row=3, column=2)

# Sort Employees
sort_button = tk.Button(window, text="Sort by Salary", command=lambda: map_employees(lambda emp: emp))
sort_button.grid(row=4, column=0)

# Extract Employee Names
extract_names_button = tk.Button(window, text="Extract Names", command=lambda: map_employees(lambda emp: emp["name"] if isinstance(emp, dict) else emp))
extract_names_button.grid(row=4, column=1)

# Calculate Total Salary
calculate_total_salary_button = tk.Button(window, text="Calculate Total Salary", command=lambda: reduce_employees(lambda x, y: x + y))
calculate_total_salary_button.grid(row=4, column=2)
result_label = tk.Label(window, text="")
result_label.grid(row=5, column=0, columnspan=3)

# Start the GUI main loop
window.mainloop()
