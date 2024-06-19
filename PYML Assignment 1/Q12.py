def sum_of_digits(number):
    # Convert number to absolute value to handle negative numbers
    number = abs(number)
    # Initialize sum to zero
    total_sum = 0
    # Iterate through each digit in the number
    while number > 0:
        # Add the last digit to the sum
        total_sum += number % 10
        # Remove the last digit from the number
        number //= 10
    return total_sum

# Example usage:
number = 12345
print(f"The sum of digits of {number} is {sum_of_digits(number)}")

number = -54321
print(f"The sum of digits of {number} is {sum_of_digits(number)}")
