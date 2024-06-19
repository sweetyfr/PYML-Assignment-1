# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    # Check if divisor is zero to avoid division by zero error
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Main function
def calculator():
    print("Welcome to Simple Calculator!")
    print("Please enter two numbers and select an operation:")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    operator = input("Enter operation (choose from +, -, *, /): ")

    result = 0
    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    else:
        print("Invalid operator! Please run the program again.")
        return

    print(f"Result: {result}")

# Run the calculator function
calculator()
