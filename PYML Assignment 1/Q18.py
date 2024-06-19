from collections import Counter

def are_anagrams(str1, str2):
    # Using Counter from collections to count occurrences of each character
    count1 = Counter(str1)
    count2 = Counter(str2)
    
    # Compare the two Counters
    if count1 == count2:
        return True
    else:
        return False

# Example usage:
string1 = "listen"
string2 = "silent"
if are_anagrams(string1, string2):
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")
