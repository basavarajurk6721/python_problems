number = [10,20,30,40 ,50]

first = number[0]

for i in range(len(number),-1):
    number[i] = number[i+1]

number[-1] = first
print("rorate list is",number)