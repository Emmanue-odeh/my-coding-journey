while True:
    try:
        print("\n==================== \n  CLI CALCULATOR      \n====================\n")
        first_number = input("Enter first number (or q to quit): ")
        if first_number == "q":
            break

        first_number = int(first_number)
        while True:

            second_number = int(input("Enter second number: "))
            operator = input("Select operator (+, -, *, /): ")
        


            if operator == "+":
                print("Result: ", first_number + second_number)

            elif operator == "-":
                print("Result: ", first_number - second_number)

            elif operator == "*":
                print("Result: ", first_number * second_number)

            elif operator == "/":
                if second_number == 0:
                    print("Cannot divide by zero")
            else:
                 print("Result: ", first_number / second_number)
        else:
         print("Invalid operator! Please use +, -, * or /.")
    
    except ValueError:
        print("Please enter a valid number!")



