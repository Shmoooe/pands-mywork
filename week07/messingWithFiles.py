# A program that counts how many times it was run.
# Data needs to be persistant.
# Author: Joanna Kelly

file_name = "count.txt"
def read_number():
    with open(file_name) as f:
        number = int(f.read())
        return number
    

def overwrite_number(number):
    with open(file_name, "wt") as f:
        f.write(str(number))
        
'''    
num = read_number()
num += 1
print (f"We have run this program {num} times")
overwrite_number(num)
'''

import os.path

'''
path = "/Users/joann/Desktop/pands/pands-mywork/week07/count.txt"
is_file = os.path.isfile(path)
print(is_file)
'''

def read_number():
    try:
        with open(file_name) as f:
            number = int(f.read())
            return number
    except IOError:
        return 0


