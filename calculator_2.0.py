# 1. Create a new file called "calculator_2.0.py"

# 2. Create a class called "Calculator" that contains the following:
# A dictionary attribute to store the available mathematical operations and their corresponding functions
# A method called "init" that initializes the dictionary with the basic mathematical operations (+, -, *, /) and corresponding functions
# A method called "add_operation" that takes in two arguments: the operation symbol and the corresponding function. This method should add the new operation and function to the dictionary.
# A method called "calculate" that takes in three arguments: the first number, the operation symbol, and the second number. This method should use the dictionary to determine the appropriate function to perform the calculation. It should also include error handling to check if the operation symbol is valid and if the input values are numbers. If an error is encountered, the method should print an error message and raise an exception.

import math

class Calculator:
    def __init__(self):
        self.operations = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide
        }

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            raise ValueError("Error: Division by zero")

    def add_operation(self, operational_symbol, function):
        self.operations[operational_symbol] = function

    def calculate(self, first_number, operational_symbol, second_number=None):
        if operational_symbol not in self.operations:
            raise ValueError(f"Error: Invalid operation '{operational_symbol}'")
        if not isinstance(first_number, (int, float)):
            raise ValueError("Invalid input! Only digits can be used.")
        if operational_symbol in ["sqrt", "log"]:
            return self.operations[operational_symbol](first_number)
        if not isinstance(second_number, (int, float)) and second_number is not None:
            raise ValueError("Invalid input! Only digits can be used.")
        calculate_function = self.operations[operational_symbol]
        return calculate_function(first_number, second_number)

# Create separate functions for the advanced mathematical operations (exponentiation, square root, logarithm) and use the "add_operation" method to add them to the calculator's dictionary.
    # Advanced mathematical operations
    def exponentiation(self, x, y):
        return x ** y

    def square_root(self, x):
        if x >= 0:
            return math.sqrt(x)
        else:
            raise ValueError("Error: Cannot compute square root of a negative number")

    def logarithm(self, x):
        if x > 0:
            return math.log(x)
        else:
            raise ValueError("Error: Cannot compute logarithm of non-positive number")


calc = Calculator()

# Add advanced operations to dictionary
calc.add_operation("^", calc.exponentiation)
calc.add_operation("sqrt", calc.square_root)
calc.add_operation("log", calc.logarithm)

# In the main program, create an instance of the Calculator class, and use a while loop that allows the user to continue performing calculations until they choose to exit.
# Use the input() function to get input from the user for the numbers and operation symbol.Use the math library for advanced mathematical operations.
# Use the isinstance() function to check if the input is a number.

while True:
    try:
        x = float(input("Enter the first number: "))
        symbol = input("Enter an operation symbol: ")
        if symbol in ["sqrt", "log"]:
            result = calc.calculate(x, symbol, None)
        else:
            y = float(input("Enter the second number: "))
            result = calc.calculate(x, symbol, y)
        print(f"Your result is: {result}")
    except:
        print("Invalid input! Only digits can be used.")

    cont = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if cont != "yes":
        break
