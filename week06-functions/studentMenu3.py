# This program will make use of the doAdd function.
# It should: read in the student's name,
# read in the module names and grades.
# create a student dict and print it out
# Author: Joanna Kelly

def display_menu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q): ").strip()

    return choice


def readModules():
    modules = []
    module_name = input("Enter the first module name (blank to quit): ")

    while module_name != " ":
        module = {}
        module["name"]= module_name
        module["grade"] = input("Enter grade: ")
        modules.append(module)
        module_name = input("enter next module name: ")
    return modules


def doAdd(students):
    current_student = {}
    current_student["name"] = input("Enter name: ")
    current_student["modules"] = readModules()

    students.append(current_student)

def display_modules(modules):
    print("\tName       \tGrade")
    for module in modules:
        print(f"\t{module['name']}  \t{module['grade']}")

def doView(students):
    for current_student in students:
        print(current_student["name"])
        display_modules(current_student["modules"])

students = []
choice = display_menu()
while(choice != "q"):
    if choice == "a":
        doAdd(students)
    elif choice == "v":
        doView(students)
    elif choice != "q":
        print("\n\nPlease select either a, v or q")
    choice=display_menu()

