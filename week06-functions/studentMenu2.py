# Taking the previous function, this program will allow the user to do more things with the program.
# e.g. the program continues to display the menu until the user picks q.
# Author: Joanna Kelly

def display_menu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q): ").strip()

    return choice
def doAdd():
    print("in adding\n")

def doView():
    print("in viewing\n")

choice = display_menu()
while(choice != "q"):
    if choice == "a":
        doAdd()
    elif choice == "v":
        doView()
    elif choice != "q":
        print("\n\nPlease select either a, v or q")
    choice=display_menu()


