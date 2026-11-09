print("====================================")
print("             SOLVEMATE")
print("      YOUR EVERYDAY PROBLEM SOLVER")
print("====================================")

print("Welcome to SolveMate!")
print("Let's work together to solve your problems.")


name = input("What is your name? ")

print(f"Nice to meet you, {name}!")

print("\nHow can I help you today?")

print("1. Money and Budgeting")
print("2. Education and Learning")
print("3. Time Management")
print("4. Technology Troubleshooting")
print("5. Personal Productivity")

choice = input("Choose an option (1-5): ")


if choice == "1":
    print("Let's help you manage your money!")

elif choice == "2":
    print("Let's improve your learning!")

elif choice == "3":
    print("Let's organize your time!")

elif choice == "4":
    print("Let's troubleshoot your technology problem!")

elif choice == "5":
    print("Let's improve your productivity!")

else:
    print("Invalid choice. Please select an option from 1 to 5.")


    income = float(input("Enter your monthly income (₦): "))

    print(f"Your monthly income is ₦{income:,.2f}")
