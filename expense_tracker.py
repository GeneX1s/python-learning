# Simple Expense Tracker

# List to store expenses
expenses = []

def add_expense(name, amount):
    """Adds an expense to the expenses list."""
    expenses.append({"name": name, "amount": amount})

def view_expenses():
    """Displays all the expenses."""
    if len(expenses) == 0:
        print("No expenses recorded yet.")
    else:
        print("\n--- Expenses ---")
        for expense in expenses:
            print(f"{expense['name']}: ${expense['amount']:.2f}")
    
def total_expenses():
    """Calculates and returns the total of all expenses."""
    total = sum(expense['amount'] for expense in expenses)
    return total

def main():
    """Main function to run the app."""
    print("Welcome to your Expense Tracker!")
    
    while True:
        print("\nChoose an option:")
        print("1. Add an expense")
        print("2. View all expenses")
        print("3. View total expenses")
        print("4. Exit")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == '1':
            name = input("Enter the name of the expense (e.g., 'Coffee', 'Transport'): ")
            try:
                amount = float(input("Enter the amount of the expense: $"))
                add_expense(name, amount)
                print(f"Added {name} - ${amount:.2f}")
            except ValueError:
                print("Please enter a valid number for the amount.")
        
        elif choice == '2':
            view_expenses()
        
        elif choice == '3':
            total = total_expenses()
            print(f"\nTotal Expenses: ${total:.2f}")
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")

# Run the app
if __name__ == "__main__":
    main()
