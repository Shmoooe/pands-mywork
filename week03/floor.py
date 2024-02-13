# A program that takes in a float and outputs an int rounded down.
# Author: Joanna Kelly

# I need the module math.floor so I imported math
# The question shows a negative number being rounded down to a positive int
# I consulted the program absolute.py to remind myself how to create an absolute number
# The initial number in the printed text must also be an absolute value.
import math

number = float(input("Enter a number: "))
absoluteValue = abs(number)
numberRoundedDown = math.floor(number)
absoluteValueFloored = abs(numberRoundedDown)

print(f"{absoluteValue} floored is {absoluteValueFloored}")

