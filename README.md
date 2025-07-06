def calculator():
    print("Simple Calculator")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    # Input operation choice
    print("Available valid operations : +  -  *  /")
    operation = input("Enter operation: ")
    # Perform calculation
    if operation == '+':
        result = num1 + num2
        print(f"The result is: {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"The result is: {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"The result is: {result}")
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"The result is: {result}")
    else:
        print("Invalid operation. Please choose from +, -, *, or /")
# Run the calculator
calculator()
