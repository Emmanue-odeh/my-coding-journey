expenses = []
expense = {
    "description": "Rice",
    "amount": 5000
}

expenses.append(expense)
print(expense)


while True:
    print("==== EXPENSE TRACKER ====")
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Show total")
    print("q. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        description = input("Enter expense description: ")
        amount = float(input("Enter expense amount: "))
        expense = {
            "description": description,
            "amount": amount
        }
        expenses.append(expense)
        print("Expense added successfully!")

    elif choice == "2":
        for expense in expenses:
          print(expense)

    elif choice == "3":
        print("Show Total selected")

    elif choice == "q":
        print("Goodbye!")
        break

    else:
        print("invalid option. Please try again.")