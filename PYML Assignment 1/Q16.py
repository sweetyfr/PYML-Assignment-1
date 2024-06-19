def count_character_frequency(input_string):
    # Initialize an empty dictionary to store character frequencies
    frequency = {}

    # Iterate through each character in the input string
    for char in input_string:
        # Increment the count of the character in the dictionary
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # Print the character frequencies
    for char, count in frequency.items():
        print(f"Character '{char}' occurs {count} times")

# Example usage:
input_string = "hello world"
count_character_frequency(input_string)
