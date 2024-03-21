# function that reads a dict from a file
# Joanna K

import json

FILENAME = "testdict.json"
def read_dict():
    with open(FILENAME) as f:
        return json.load(f)
    
some_dict = read_dict()
print(some_dict)

