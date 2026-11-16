numbers = [[1, 2], [3, 4], [5, 6]]

result = []

for sublist in numbers:
    for num in sublist:
        result.append(num)
print("original list is :",numbers)
print("flattened list is :",result)