def find_largest(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num
    return largest

number = list(map(int,input("Enter the numbers :").split()))
result = find_largest(number)
print(f"largest number is : {result}")