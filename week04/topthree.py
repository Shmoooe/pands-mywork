# This program generates 10 random numbers between 0 and 100.
# It then prints them out then prints out the top three.

# Author: Joanna Kelly

import random

numbers = []

for i in range(0, 10):
    numbers.append(random.randint(0,100))
    print(f"10 random numbers: {numbers}")

top_ones = numbers.copy()

top_ones.sort(reverse = True)
print(f"The top 3 numbers are {top_ones[0:3]}")