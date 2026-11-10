num = int(input("Enter a positive integer: "))
original = abs(num)  # Ensure the number is positive
reverse = 0

while original > 0:
    digit = original % 10
    reverse = reverse * 10 + digit
    original = original // 10

if num < 0:
    reverse = -reverse

print(f"The reverse of the given number is: {reverse}")
