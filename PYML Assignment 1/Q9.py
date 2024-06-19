#python program that checks if a substring is present in a given string
def check_substring(main_string, substring):
    if substring in main_string:
        return True
    else:
        return False

# Example usage:
main_string = "Hello, welcome to the world of Python!"
substring = "welcome"

if check_substring(main_string, substring):
    print(f"The substring '{substring}' is present in the main string.")
else:
    print(f"The substring '{substring}' is not present in the main string.")
