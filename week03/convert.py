# A program to convert a float number to an absolute value to be presented in cents
# Author: Joanna Kelly

import math

first_amount = float(input("Please enter an amount: "))
absolute_first_amount = abs(first_amount)

amount_in_cent = int(absolute_first_amount * 100)

print(f"That amount in cent is: {amount_in_cent}")

