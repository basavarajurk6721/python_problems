minimum = lambda a ,b ,c : a if a < b and a < c else b if b < c else c

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
num3 = int(input("Enter third number : "))

result = minimum(num1,num2,num3)
print(f"minimum number is : {result}")