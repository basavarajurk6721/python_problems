list1 = [10, 20, 30, 40, 50]
list2 = [20, 40, 60, 80]

result = []

for num in list1:
    if num not in list2:
        result.append(num)

print("list1 is:",list1)
print("list2 is ",list2)
print("result is",result)