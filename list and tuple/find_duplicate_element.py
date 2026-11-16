numbers = [10, 20, 30, 10, 40, 20, 50, 10]

duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("original list is:",numbers)
print("duplicate elements:",duplicates)