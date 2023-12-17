def sum(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiplication (x, y):
    return x * y

def division (x, y):
    if y != 0:
        return x / y
    else:
        return "not divide by 0"

def calculator():
    try:
        num1 = float(input("Enter the num1: "))
        num2 = float(input("Enter the num2: "))
        operation = input("Enter operation (+, -, *, /): ")

        if operation == '+':
            result = sum(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiplication (num1, num2)
        elif operation == '/':
            result = division (num1, num2)
        else:
            result = "Invalid operation"

        print(f"Result: {result}")

    except ValueError:
        print("Please enter valid numeric values.")

calculator()