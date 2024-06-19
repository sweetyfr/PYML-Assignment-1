def starts_or_ends(string, prefix=None, suffix=None):
    starts_with_prefix = False
    ends_with_suffix = False

    if prefix is not None:
        starts_with_prefix = string.startswith(prefix)

    if suffix is not None:
        ends_with_suffix = string.endswith(suffix)

    return starts_with_prefix, ends_with_suffix

# Example usage:
input_string = "Hello, World!"
prefix_to_check = "Hello"
suffix_to_check = "World!"

starts_with, ends_with = starts_or_ends(input_string, prefix_to_check, suffix_to_check)

if starts_with:
    print(f"The string '{input_string}' starts with the prefix '{prefix_to_check}'.")
else:
    print(f"The string '{input_string}' does not start with the prefix '{prefix_to_check}'.")

if ends_with:
    print(f"The string '{input_string}' ends with the suffix '{suffix_to_check}'.")
else:
    print(f"The string '{input_string}' does not end with the suffix '{suffix_to_check}'.")
