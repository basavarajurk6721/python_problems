student = {
    "name" : "basava",
    "age" : "21",
    "branch" : "ECE"
}

inverted = {}

for key, value in student.items():
    inverted[value] = key

print("original dictionary is :",student)
print("inverted dictionary is :",inverted)