while True:
    print("==== EXPENSE TRACKER ====")
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Show total")
    print("q. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Add Expense selected")

    elif choice == "2":
        print("View Expenses selected")

    elif choice == "3":
        print("Show Total selected")

    elif choice == "q":
        print("Goodbye!")
        break

    else:
        print("invalid option. Please try again.")