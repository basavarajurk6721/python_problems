def find_gcd(a,b):
    smaller = min(a,b)
    gcd = 1

    for i in range(1, smaller+1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd
num1 = int(input("Enter a number :"))
num2 = int(input("Enter a number :"))

result = find_gcd(num1,num2)
print(f"GCD is : {result}")