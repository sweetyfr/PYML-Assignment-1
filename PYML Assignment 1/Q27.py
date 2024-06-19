def string_to_list(input_string):
    # Using list comprehension to convert string to list of characters
    characters_list = [char for char in input_string]
    return characters_list

# Example usage:
input_string = "Hello, World!"
characters_list = string_to_list(input_string)
print(characters_list)
