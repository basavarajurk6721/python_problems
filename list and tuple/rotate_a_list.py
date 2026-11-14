numbers = [20 ,40 ,50 ,60 ,70 ,80]
last_element = numbers[-1]

for i in range(len(numbers)-1,0,-1):
    numbers[i] = numbers[i-1]
    numbers[0] = last_element
print(f"the rotated number is{numbers}")