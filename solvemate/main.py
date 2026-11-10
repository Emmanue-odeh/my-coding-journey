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

try:
    income = float(input("Enter your monthly income (₦): "))
except ValueError:
    print("Please enter a valid number.")

    
print(f"Your monthly income is ₦{income:,.2f}")


food = float(input("How much do you spend on food monthly? ₦"))

transport = float(input("How much do you spend on transportation monthly? ₦"))

electricity = float(input("How much do you spend on electricity monthly? ₦"))

internet = float(input("How much do you spend on internet monthly? ₦"))

total_expenses = food + transport + electricity + internet

print(f"Your total monthly expenses are: ₦{total_expenses:,.2f}")

remaining_balance = income - total_expenses

print(f"Your remaining balance is: ₦{remaining_balance:,.2f}")


if remaining_balance > 0:
    print("Great! You have money left. Consider saving some of it.")

elif remaining_balance == 0:
    print("You have spent all your monthly income.")

else:
    print("Warning! Your expenses are higher than your income.")
