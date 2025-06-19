 def calculator():
    print("Welcome to the Simple Calculator!")
    
    # Get user input for numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Show available operations
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Get user input for operation
    operation = input("Enter the operation symbol (+, -, *, /): ")

    # Perform calculation
    if operation == '+':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation selected.")

  