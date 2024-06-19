def max_min(numbers):
    max_num = max(numbers)
    min_num = min(numbers)
    return min_num, max_num

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("Minimum and maximum values in the given list of numbers is", max_min(numbers))