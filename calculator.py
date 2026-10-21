#A calculator

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b

def power(a,b):
    return a ** b

def calculator():
    print("=========================")
    print("WELCOME TO MINI CALCULATOR")
    print("=========================")
    print("Select operation: +, -, *, /, **")
    print("Type 'quit' at any prompt to exit. \n")


    while True:

        first_input = input("Enter first number (or 'quit'): ").strip()
        if first_input.lower() == 'quit':
            print("Goodbye!")
            break

        try:
            num1 = float(first_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        op = input("Enter operation (+, -, *, /, **): ").strip()
        if op.lower() == 'quit':
            print("Goodbye!")
            break

        if op not in ['+', '-', '*', '/', '**']:
            print("Invalid operation. Please select from +, -, *, /, **.")
            continue

        second_input = input("Enter second number (or 'quit'): ").strip()
        if second_input.lower() == 'quit':
            print("Goodbye!")
            break

        try:
            num2 = float(second_input)
        except ValueError:
            print("Invalid input. Please enter a valid number. \n")
            continue


        try:
            if op == "+":
                result = add(num1, num2)
            elif op == "-":
                result = subtract(num1, num2)
            elif op == "*":
                result = multiply(num1, num2)
            elif op == "/":
                result = divide(num1, num2)
            elif op == "**":
                result = power(num1, num2)

            if isinstance(result, float) and not isinstance(result, complex) and result.is_integer():
                result = int(result)

            print(f"Result: {num1:g} {op} {num2:g} = {result}\n")

        except ZeroDivisionError as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    calculator()