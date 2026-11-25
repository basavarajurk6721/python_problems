def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
number = int(input("Ennter a number :"))
if number < 0:
    print("pleace enter non negative number :")
else:
    result = fibonacci(number)
    print(f"fibonacci number at position {number} : {result}")