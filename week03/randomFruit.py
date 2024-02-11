# This program prints out a random fruit
# Author: Joanna Kelly

import random

fruits = ["Apple", "Orange", "Banana", "Pear"]

index = random.randint(0, len(fruits)-1)

fruit = fruits[index]

print(f"A random fruit: {fruit}")

