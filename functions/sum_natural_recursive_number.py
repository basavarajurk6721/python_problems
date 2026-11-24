def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n-1)

number = int(input("Enter a number :"))
result = sum_natural(number)
print(f"sum of natural number is : {result}")