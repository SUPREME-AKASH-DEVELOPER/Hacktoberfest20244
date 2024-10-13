# simple_calculator.py
# This script implements a simple command-line calculator in Python.
# It can perform basic arithmetic operations: addition, subtraction, multiplication, and division.

def add(x, y):
    """Return the sum of x and y."""
    return x + y

def subtract(x, y):
    """Return the difference of x and y."""
    return x - y

def multiply(x, y):
    """Return the product of x and y."""
    return x * y

def divide(x, y):
    """Return the quotient of x and y. Raises ValueError if dividing by zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def calculator():
    """Main function to run the calculator."""
    print("Welcome to the Simple Calculator!")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        choice = input("Enter choice (1/2/3/4) or 'q' to quit: ")

        if choice == 'q':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))  # Get first number from user
                num2 = float(input("Enter second number: "))  # Get second number from user

                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")  # Perform addition
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")  # Perform subtraction
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")  # Perform multiplication
                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")  # Perform division
            except ValueError as e:
                print(f"Error: {e}")  # Handle invalid inputs
        else:
            print("Invalid input. Please enter a number between 1-4.")

if __name__ == "__main__":
    calculator()

'''
Features:
---------
1. **Addition**: Adds two numbers.
2. **Subtraction**: Subtracts the second number from the first.
3. **Multiplication**: Multiplies two numbers.
4. **Division**: Divides the first number by the second, with error handling for division by zero.

Usage:
------
To run the calculator, execute the script in a Python environment. 
Follow the prompts to perform arithmetic operations. 
You can type 'q' at any time to exit the program.
'''
