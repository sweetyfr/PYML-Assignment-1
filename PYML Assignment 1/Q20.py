def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Example usage:
num_list = [1, 2, 3, 4, 5]
result = sum_of_list(num_list)
print(f"The sum of {num_list} is: {result}")
