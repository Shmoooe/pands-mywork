# A program that reads in a string and strips any leading or trailing spaces, converts any non-lower case letters to lower case.
# Program also outputs the length of the input and output strings.
# Author: Joanna Kelly

inputString = input("Please enter a string: ")
normalisedString = inputString.strip().lower()

lengthOfInput = len(inputString)
lengthOfNormalisedString = len(normalisedString)

print(f"That string normalised is: {normalisedString}\nWe reduced the input string from {lengthOfInput} to {lengthOfNormalisedString}")

