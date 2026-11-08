student = int(input("Enter a student marks:"))

if student < 0 or student > 100:
    print("Invalid marks")
elif student >= 90:
    print("Grade A")
elif student >= 80:
    print("Grade B")
elif student >= 70:
    print("Grade C")
elif student >= 60:
    print("Grade D")
elif student >= 35:
    print("Grade E")
else:
    print("Grade F")