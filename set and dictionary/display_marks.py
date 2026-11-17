students = {
    "Rahul": 85,
    "Arun": 65,
    "Kiran": 90,
    "Ravi": 72,
    "Anu": 80
}

print("Students who scored above 75:")

for name, marks in students.items():
    if marks > 75:
        print(name, ":", marks)