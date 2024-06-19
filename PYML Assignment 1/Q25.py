def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                destination.write(source.read())
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print("One of the files does not exist.")
    except IOError:
        print("Error reading or writing to file.")

# Example usage:
source_file = 'source.txt'
destination_file = 'destination.txt'
copy_file(source_file, destination_file)
