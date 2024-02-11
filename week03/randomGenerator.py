# Program that prints out a random number between 1 and 10
# Author: Joanna Kelly

import random

x = int(input("Enter the minimum range value: "))
y = int(input("Enter the maximum range value: "))
number = random.randrange(x,y)

print(f"Here is a random number {number}")

