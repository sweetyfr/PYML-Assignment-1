def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

# Example usage:
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 2, 2, 3, 1, 4, 5, 2]
    target_element = 2

    occurrences = count_occurrences(my_list, target_element)
    print(f"The element {target_element} occurs {occurrences} times in the list.")
