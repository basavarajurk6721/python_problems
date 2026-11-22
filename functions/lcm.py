def find_lcm(a, b):
    larger = max(a, b)

    while True:
        if larger % a == 0 and larger % b == 0:
            return larger
        larger += 1
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = find_lcm(num1, num2)
print("LCM:", result) 