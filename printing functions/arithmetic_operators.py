num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")

if num2 != 0:
    print(f"Division: {num1 / num2}")
    print(f"Modulus: {num1 % num2}")
else:
    print("Division and Modulus by zero is not allowed.")