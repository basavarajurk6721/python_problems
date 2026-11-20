def calculate_sum(numbers):
    total = 0

    for num in numbers:
        total += num

    return total
numbers = list(map(int, input("Enter a number :").split()))
result = calculate_sum(numbers)
print(f"sum of elements : {result}")