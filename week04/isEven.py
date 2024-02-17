# a program that tells the user if the input is an even or an odd number.
# Author: Joanna Kelly

number = int(input("Enter a number: "))
if (number % 2) == 0:
    print(f"{number} is an even number")
elif (number % 2) != 0:
    print(f"{number} is an odd number")



