numbers = [1, 2, 3, 5, 6, 7]
n = 7

total = n * (n +1) // 2
actul_sum = 0

for num in numbers:
    actul_sum += num

missing_number = total- actul_sum
print("missing number is :",missing_number)