# Stores students information to a dictionary and then prints it out.
# Author: Joanna K


mary = {
    "name":"Mary",
    "modules": [
        {
            "courseName":"Programming",
            "grade": 45
        },
        {
            "courseName":"History",
            "grade": 99
        }
    ]

}
print("Student: {}".format(mary["name"]))
for module in mary["modules"]:
    print("\t {} \t: {}".format(module["courseName"], module["grade"]))



