# Function to calculate the length of a string
def string_length(input_string):
    return len(input_string)

# Main function to get user input and print the length
def main():
    user_input = input("Enter a string: ")
    length = string_length(user_input)
    print(f"The length of the string is: {length}")

# Entry point of the program
if __name__ == "__main__":
    main()
