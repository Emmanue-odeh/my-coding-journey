expenses = []

while True:
    print("==== EXPENSE TRACKER ====")
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("q. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        description = input("Enter expense description: ").strip()

        if not description:
            print("Description cannot be empty!")
            continue

        try:
            amount = float(input("Enter expense amount: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if amount <= 0:
            print("Amount must be greater than zero!")
            continue

        expense = {
            "description": description,
            "amount": amount
        }

        expenses.append(expense)
        print("Expense added successfully!")

    elif choice == "2":
        if not expenses:
            print("No expenses recorded yet.")
        else:
            for index, expense in enumerate(expenses, 1):
                print(f"{index}. {expense['description']} - ₦{expense['amount']:.2f}")

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)
        print(f"Total expenses: ₦{total:.2f}")

    elif choice == "q":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
