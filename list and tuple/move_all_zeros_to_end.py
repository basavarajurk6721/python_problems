number = [10,0,20,0,30,0,40,0,50,0]
result = []

for num in number:
    if num != 0:
        result.append(num)

zero_count = number.count(0)
for i in range(zero_count):
    result.append(0)
print("original list is :",number)
print("updated list is :",result)