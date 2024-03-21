# a function that will store a simple Dict to a file as JSON.
# Author: Joanna K

import json

FILENAME = "testdict.json"
sample = dict(name= "Fred", age= 31, grades= [1, 34, 55])

def write_dict(obj):
    with open(FILENAME, "wt") as f:
        json.dump(obj, f)

write_dict(sample)