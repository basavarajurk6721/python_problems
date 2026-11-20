def check_prime(num):
    if num <= 1:
        return False

    for i in range(2,num):
        if num % i == 0:
            return False
    return True
number = int(input("Enter a number :"))
result = check_prime(number)

if result:
    print(f"{number} is prime number")
else:
    print(f"{number} is not a prime number ")