dict1 = {
    "name": "Rahul",
    "age": 21,
    "branch": "ECE",
    "college": "KVGCE"
}

dict2 = {
    "name": "Arun",
    "age": 22,
    "city": "Mysore",
    "course": "Engineering"
}

common_keys = []

for key in dict1:
    if key in dict2:
        common_keys.append(key)

print("Common keys:", common_keys)