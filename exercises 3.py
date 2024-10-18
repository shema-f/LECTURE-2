import random

#qn1. Generate 100 random integers between 1 and 50
random_integers = [random.randint(1, 50) for _ in range(100)]

# Print the list of random integers
print(random_integers)

import random
import statistics

# Generate 100 random integers between 1 and 50
random_integers = [random.randint(1, 50) for _ in range(100)]
# qn2 compute mean ,median,mode,and standard deviation
# Compute statistics
mean = statistics.mean(random_integers)
median = statistics.median(random_integers)
mode = statistics.mode(random_integers)
stdev = statistics.stdev(random_integers)

# Print the statistics
print(f"Random Integers: {random_integers}")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Standard Deviation: {stdev}")

