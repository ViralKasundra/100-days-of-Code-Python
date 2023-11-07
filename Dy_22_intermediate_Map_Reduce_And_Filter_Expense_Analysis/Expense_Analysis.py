from functools import reduce

def apply_tax(expense, tax_rate):
    return expense * (1 + tax_rate)

def calculate_total(expense1, expense2):
    return expense1 + expense2

def is_expensive(expense, threshold):
    return expense > threshold

expenses = []
tax_rate = float(input("Enter the tax rate (e.g., 0.10 for 10%): "))
threshold = float(input("Enter the expense threshold for high expenses: "))

while True:
    expense = float(input("Enter an expense amount (or enter 0 to finish): "))
    if expense == 0:
        break
    expenses.append(expense)

taxed_expenses = list(map(lambda exp: apply_tax(exp, tax_rate), expenses)
total_expenses = reduce(calculate_total, taxed_expenses)
high_expenses = list(filter(lambda exp: is_expensive(exp, threshold), taxed_expenses)

print("Original Expenses:", expenses)
print("Expenses After Tax:", taxed_expenses)
print("Total Expenses:", total_expenses)
print(f"High Expenses (> ${threshold:.2f}):", high_expenses)

# Sort expenses in ascending order
sorted_expenses = sorted(taxed_expenses)
print("Sorted Expenses (Ascending):", sorted_expenses)

# Calculate and display the average expense
average_expense = total_expenses / len(expenses)
print(f"Average Expense: ${average_expense:.2f}")

# Allow the user to modify or remove specific expenses
while True:
    action = input("Do you want to modify or remove an expense? (M/R/None): ").strip().lower()
    if action == "none":
        break
    elif action == "m":
        index = int(input("Enter the index of the expense you want to modify: "))
        new_expense = float(input("Enter the new expense amount: "))
        expenses[index] = new_expense
        print("Expenses updated.")
    elif action == "r":
        index = int(input("Enter the index of the expense you want to remove: "))
        removed_expense = expenses.pop(index)
        print(f"Expense {removed_expense:.2f} removed.")

# Updated results
taxed_expenses = list(map(lambda exp: apply_tax(exp, tax_rate), expenses)
total_expenses = reduce(calculate_total, taxed_expenses)
high_expenses = list(filter(lambda exp: is_expensive(exp, threshold), taxed_expenses)
sorted_expenses = sorted(taxed_expenses)
average_expense = total_expenses / len(expenses)

print("Updated Expenses:", expenses)
print("Expenses After Tax (Updated):", taxed_expenses)
print("Total Expenses (Updated):", total_expenses)
print(f"High Expenses (> ${threshold:.2f}) (Updated):", high_expenses)
print("Sorted Expenses (Ascending) (Updated):", sorted_expenses)
print(f"Average Expense (Updated): ${average_expense:.2f}")

