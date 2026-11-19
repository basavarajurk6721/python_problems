def count_digits(num):
    count = 0

    if num == 1:
        return 1
    while num != 0:
        num = num // 10
        count += 1
    return count

number = int(input("Enter a number :"))
result = count_digits(number)
print(f"number of digits is : {result}")