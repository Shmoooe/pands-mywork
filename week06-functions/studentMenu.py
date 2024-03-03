# This program uses a function to print out a menu of commands we can perform,
# e.g. add, view and quit
# the function then returns what the user chose.
# Author: Joanna Kelly

def display_menu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q): ").strip()

    return choice

choice = display_menu()
print(f"You chose {choice}")
