def square(num):
    return num ** 2

numbers = [2, 4, 6, 8, 10]

result = list(map(square,numbers))

print("Original list:", numbers)
print("Squared numbers:", result)