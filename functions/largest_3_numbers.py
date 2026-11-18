def largest_number(a, b, c):
    if a >= b and a >=c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

a = int(input("Enter a first number :"))
b = int(input("Enter a second number :"))
c = int(input("Enter a third number :"))

result = largest_number(a, b, c)
print(f"largest number is : {result}")