import json
import os

# Initialize transaction storage
def initialize_storage():
    if not os.path.exists("transactions.json"):
        with open("transactions.json", "w") as file:
            json.dump([], file)

# Add a transaction
def add_transaction(transaction):
    with open("transactions.json", "r") as file:
        transactions = json.load(file)
    transactions.append(transaction)
    with open("transactions.json", "w") as file:
        json.dump(transactions, file)

# Get transactions
def get_transactions():
    with open("transactions.json", "r") as file:
        transactions = json.load(file)
    return transactions

# Get income and expenses
def get_income_and_expenses():
    transactions = get_transactions()
    income = 0
    expenses = 0
    for transaction in transactions:
        if transaction["type"] == "income":
            income += transaction["amount"]
        else:
            expenses += transaction["amount"]
    return income, expenses

# Get remaining budget
def get_remaining_budget():
    income, expenses = get_income_and_expenses()
    return income - expenses

# Analyze expenses
def analyze_expenses():
    transactions = get_transactions()
    expense_categories = {}
    for transaction in transactions:
        if transaction["type"] == "expense":
            category = transaction["category"]
            amount = transaction["amount"]
            if category in expense_categories:
                expense_categories[category] += amount
            else:
                expense_categories[category] = amount
    return expense_categories

# Main loop
def main():
    initialize_storage()
    while True:
        print("\nBudget Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Remaining Budget")
        print("4. Analyze Expenses")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            amount = float(input("Enter income amount: "))
            add_transaction({"type": "income", "amount": amount})
        elif choice == "2":
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            add_transaction({"type": "expense", "amount": amount, "category": category})
        elif choice == "3":
            print("Remaining Budget: ", get_remaining_budget())
        elif choice == "4":
            print("Expense Analysis: ")
            for category, amount in analyze_expenses().items():
                print(f"{category}: {amount}")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
