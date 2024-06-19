# Get user input
user_input = input("Please enter a string: ")

# Specify the filename
filename = "user_input.txt"

# Open the file in write mode and write the user input to the file
with open(filename, "w") as file:
    file.write(user_input)

print(f"The input has been written to {filename}")
