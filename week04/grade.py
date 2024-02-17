# A program that reads in a student's percentage mark and prints out the corresponding grade.
# Author: Joanna Kelly

grade = int(input("Enter the percentage: "))

if grade < 40:
    print(f"Fail")
elif grade >= 40 and grade <= 49:
    print(f"Pass")
elif grade >= 50 and grade <= 59:
    print(f"Merit 2")
elif grade >= 60 and grade <= 69:
    print(f"Merit 1")
elif grade >= 70:
    print(f"Distinction")
