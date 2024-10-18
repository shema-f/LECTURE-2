def is_prime(n):
    if n <= 1:
        return False  # 0 and 1 are not prime numbers
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # Found a divisor, not a prime number
    return True  # No divisors found, it is a prime number

# Get user input
try:
    user_input = int(input("Enter a positive integer: "))
    if is_prime(user_input):
        print(f"{user_input} is a prime number.")
    else:
        print(f"{user_input} is not a prime number.")
except ValueError:
    print("Invalid input! Please enter a positive integer.")
