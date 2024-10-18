def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    
    # Check if the string is the same forwards and backwards
    return s == s[::-1]

# Example usage
print(is_palindrome("madam"))       
print(is_palindrome("hello"))        
print(is_palindrome("A man a plan a canal Panama"))  
