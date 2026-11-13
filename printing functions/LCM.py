num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 == 0 or num2 == 0:
    lcm = 0
else:
    for i in range(max(abs(num1), abs(num2)), abs(num1 * num2) + 1):
        if i % abs(num1) == 0 and i % abs(num2) == 0:
            lcm = i
            break
print(f"The LCM of {num1} and {num2} is: {lcm}")