def is_prime(num):
    if num < 1:
        return False
    for i in range(2 ,int(num ** 0.5)+1):
        if num % i == 0:
            return False
        return True
numbers = [2, 4, 5, 7, 9, 11, 15, 17, 20, 23]
result = list(filter(lambda num:is_prime(num) ,numbers))
print(f"original list : {numbers}")
print(f"even numbers : {result}")