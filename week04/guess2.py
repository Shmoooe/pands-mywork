# a program that prompts the user to make a guess as to what the chosen number it.
# This program will tell the user if their guess was too high or too low.

import random

the_chosen_one = random.randint(1, 100)

guess = int(input("Please guess the number: "))

while guess != the_chosen_one:
    if guess < the_chosen_one:
        print ("Too low")
    else:
        print ("Too high")
    guess = int(input("Please guess again: "))

print(f"Well done! Yes the number was {the_chosen_one}")
