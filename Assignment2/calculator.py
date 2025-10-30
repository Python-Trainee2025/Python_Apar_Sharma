try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")

    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        if b == 0:
            print("Error: Division by zero.")
            result = None
        else:
            result = a / b
    else:
        print("Error: Invalid operator.")
        result = None

    if result is not None:
        print("Result:", result)

except ValueError:
    print("Error: Please enter valid numbers.")