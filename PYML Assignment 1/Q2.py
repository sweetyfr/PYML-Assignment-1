# Function to check if a number is even or odd
def check_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Input from the user
number = int(input("Enter a number: "))

# Check if the number is even or odd
result = check_even_or_odd(number)

# Output the result
print(f"The number {number} is {result}.")
