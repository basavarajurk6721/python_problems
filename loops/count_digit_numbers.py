num = int(input("Enter a positive integer: "))
num = abs(num)  # Ensure the number is positive
count = 0
if num == 0:
    count = 1
else:
    while num > 0:
        num //= 10
        count += 1
print(f"The number of digits in the given number is: {count}")