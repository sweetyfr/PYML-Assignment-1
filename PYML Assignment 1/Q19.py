import string

def remove_punctuation(input_string):
    # Create a translation table that maps each punctuation character to None
    translator = str.maketrans('', '', string.punctuation)
    
    # Use the translation table to remove punctuation
    clean_string = input_string.translate(translator)
    
    return clean_string

# Example usage:
input_string = "Hello, World! This is a test string. Let's remove punctuation!"
cleaned_string = remove_punctuation(input_string)
print("Original string:")
print(input_string)
print("\nString with punctuation removed:")
print(cleaned_string)
