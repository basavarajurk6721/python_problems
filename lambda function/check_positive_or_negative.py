check_nuner = lambda num : "positive" if num > 0 else "negative" if num < 0 else "zero"
number = int(input("Enter a numbe : "))
result = check_nuner(number)
print(f"number is : {result}")