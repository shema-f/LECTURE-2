def is_perfect_number(n):
    if n < 1:
        return False
    
    sum_of_divisors = 0
    # Loop through potential divisors
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            sum_of_divisors += i
            
    return sum_of_divisors == n

# Print all perfect numbers between 1 and 1,000,000
print("Perfect numbers between 1 and 1,000,000:")
for num in range(1, 1000001):
    if is_perfect_number(num):
        print(num)
