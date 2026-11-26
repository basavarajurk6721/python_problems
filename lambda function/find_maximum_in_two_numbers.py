maximum = lambda a,b:a if a > b else b
num1 = int(input("Enter a first num : "))
num2 = int(input("Enter a second num : "))

result = maximum(num1,num2)
print(f"maximum number is : {result}")