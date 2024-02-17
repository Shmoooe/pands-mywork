# A program that prompts the user to guess a random number until the user lands on the right one.
# Author: Joanna Kelly

the_chosen_one = 69
guess = int(input("Please guess the number: "))

while guess != the_chosen_one:
    print(f"Wrong")
    guess = int(input("Please guess again: "))

print(f"Well done! Yes the number was {the_chosen_one}")


