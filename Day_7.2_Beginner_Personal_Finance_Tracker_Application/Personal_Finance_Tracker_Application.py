import json


class Transaction:
    def __init__(self, date, description, category, amount):
        self.date = date
        self.description = description
        self.category = category
        self.amount = amount


class PersonalFinanceTracker:
    def __init__(self):
        self.transactions = []
        self.budgets = {}

    def add_transaction(self, transaction):
        if not isinstance(transaction.amount, (int, float)):
            raise ValueError("Amount must be a number.")
        self.transactions.append(transaction)

    def view_transactions(self):
        for transaction in self.transactions:
            print(
                f"Date: {transaction.date}, Description: {transaction.description}, Category: {transaction.category}, Amount: {transaction.amount}")

    def calculate_total_balance(self):
        income = sum(transaction.amount for transaction in self.transactions if transaction.amount > 0)
        expenses = sum(transaction.amount for transaction in self.transactions if transaction.amount < 0)
        return income - expenses

    def calculate_category_spending(self, category):
        category_expenses = sum(
            transaction.amount for transaction in self.transactions if transaction.category == category)
        return category_expenses

    def set_budget(self, category, budget_limit):
        self.budgets[category] = budget_limit

    def view_budgets(self):
        for category, budget_limit in self.budgets.items():
            print(f"Category: {category}, Budget Limit: {budget_limit}")

    def check_budget(self, category):
        if category in self.budgets:
            category_expenses = sum(
                transaction.amount for transaction in self.transactions if transaction.category == category)
            budget_limit = self.budgets[category]
            return category_expenses, budget_limit
        else:
            return None, None

    def save_data(self, filename):
        data = {
            "transactions": [
                {
                    "date": transaction.date,
                    "description": transaction.description,
                    "category": transaction.category,
                    "amount": transaction.amount,
                }
                for transaction in self.transactions
            ],
            "budgets": self.budgets
        }
        with open(filename, "w") as file:
            json.dump(data, file)
        print(f"Data saved to '{filename}'.")

    def load_data(self, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.transactions = [
                    Transaction(
                        item["date"],
                        item["description"],
                        item["category"],
                        item["amount"],
                    )
                    for item in data.get("transactions", [])
                ]
                self.budgets = data.get("budgets", {})
                print(f"Data loaded from '{filename}'.")
        except FileNotFoundError:
            print("File not found. Unable to load data.")
        except json.JSONDecodeError:
            print("Invalid JSON format in the file. Unable to load data.")


def initialize_budgets(finance_tracker):
    # Initialize budgets for different categories
    finance_tracker.set_budget("Groceries", 300.0)
    finance_tracker.set_budget("Rent", 1200.0)
    finance_tracker.set_budget("Transportation", 150.0)
    finance_tracker.set_budget("Entertainment", 200.0)


def initialize_data(finance_tracker):
    # Initialize some transactions
    transaction1 = Transaction("2023-01-05", "Groceries", "Food", -50.0)
    transaction2 = Transaction("2023-01-10", "Paycheck", "Income", 1500.0)
    transaction3 = Transaction("2023-01-15", "Rent", "Housing", -800.0)

    finance_tracker.add_transaction(transaction1)
    finance_tracker.add_transaction(transaction2)
    finance_tracker.add_transaction(transaction3)

    # Initialize some budgets
    finance_tracker.set_budget("Food", 200.0)
    finance_tracker.set_budget("Housing", 1000.0)


def main():
    finance_tracker = PersonalFinanceTracker()

    # Initialize data
    initialize_data(finance_tracker)
    # Initialize budgets
    initialize_budgets(finance_tracker)

    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Calculate Total Balance")
        print("4. Calculate Category Spending")
        print("5. Set Budget")
        print("6. View Budgets")
        print("7. Check Budget")
        print("8. Save Data")
        print("9. Load Data")
        print("10. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8/9/10): ")

        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD): ")
            description = input("Enter a description: ")
            category = input("Enter a category: ")
            try:
                amount = float(input("Enter the amount: "))
                transaction = Transaction(date, description, category, amount)
                finance_tracker.add_transaction(transaction)
                print("Transaction added successfully!")
            except ValueError:
                print("Invalid amount. Please enter a valid number.")

        if choice == '2':
            if finance_tracker.transactions:
                finance_tracker.view_transactions()
            else:
                print("No transactions to display.")

        elif choice == '3':
            total_balance = finance_tracker.calculate_total_balance()
            print(f"Total Balance: {total_balance}")

        elif choice == '4':
            category = input("Enter the category to calculate spending: ")
            category_spending = finance_tracker.calculate_category_spending(category)

            if category_spending is not None:
                print(f"Category '{category}' does not exist or has no spending.")
            else:
                print(f"Spending in '{category}': {category_spending}")

        elif choice == '5':
            category = input("Enter the category to set a budget: ")
            budget_limit = float(input("Enter the budget limit: "))
            finance_tracker.set_budget(category, budget_limit)
            print(f"Budget set for '{category}' with a limit of {budget_limit}")

        elif choice == '6':
            finance_tracker.view_budgets()

        elif choice == '7':
            category = input("Enter the category to check the budget: ")
            category_expenses, budget_limit = finance_tracker.check_budget(category)
            if category_expenses is not None:
                if category_expenses > budget_limit:
                    print(f"Category '{category}' has exceeded its budget of {budget_limit}.")
                else:
                    print(f"Category '{category}' is within its budget of {budget_limit}.")
            else:
                print(f"No budget set for category '{category}'.")

        elif choice == '8':
            filename = input("Enter the filename for data: ")
            finance_tracker.save_data(filename)

        elif choice == '9':
            filename = input("Enter the filename to load data from: ")
            finance_tracker.load_data(filename)

        elif choice == '10':
            print("Exiting the Personal Finance Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option (1/2/3/4/5/6/7/8/9/10).")

if __name__ == "__main__":
    main()
