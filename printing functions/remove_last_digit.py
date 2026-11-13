num = int(input("Enter a number: "))

remove_last_digit = abs(num) // 10

if num < 0:
    remove_last_digit = -remove_last_digit

print(f"The number after removing the last digit of {num} is: {remove_last_digit}")