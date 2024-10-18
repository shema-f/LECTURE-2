def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if sorted characters are the same
    return sorted(str1) == sorted(str2)

# Example usage
string1 = "listen"
string2 = "enlist"

result = are_anagrams(string1, string2)
print(result)  # Output: True
