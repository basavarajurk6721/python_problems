def check_even_odd(num):
    if num % 2 == 0:
        return "even number"
    else:
        return "odd number"

num = int(input("Enter a number:"))
reult = check_even_odd(num)
print(f"{num} is {reult}")