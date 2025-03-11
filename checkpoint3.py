def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

# a calculator to perform the operations
def calculator():
    should_continue = True
    first_number = float(input("Enter the first number: "))
    print("these are the available operations: ")
    for operation_symbol in operations.keys():
        print(operation_symbol)
    while should_continue:
        operation_symbol = input("pick an operation: ")
        if operation_symbol not in operations:
            print("Invalid operation")
            continue
        else:
            second_number = float(input("enter the second number: "))

            calculation_function = operations[operation_symbol]
            answer = calculation_function(first_number, second_number)
            print(f"{first_number} {operation_symbol} {second_number} = {answer}")
            choice = input("do you want to continue with the result as the first number? Type 'yes' or 'no'")
            if choice == 'yes':
                first_number = answer
            elif choice == 'no':
                should_continue = False
                calculator()
            elif choice == "stop":
                print("Thank you for using the calculator")
                break
            else:
                print("invalid input,the available choice are (yes, no, stop)")


calculator()

