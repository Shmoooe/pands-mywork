# To divide the first number by the second provide the integer result and the remainder.
# Author: Joanna Kelly

x = int(input("Enter first number: "))
y = int(input("Enter the number you want to divide by: "))

answer = int(x//y)
remainder = x%y

print(f"{x} divided by {y} is {answer} with remainder {remainder}")


