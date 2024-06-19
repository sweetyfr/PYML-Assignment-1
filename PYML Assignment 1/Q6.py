def read_and_print_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the path to your file
file_path = 'path/to/your/file.txt'

# Call the function to read and print the file content
read_and_print_file(file_path)
