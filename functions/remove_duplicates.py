def remove_duplicates(numbers):
    unique_numbers = []

    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers
numbers = list(map(int, input("Enter a number").split()))
result = remove_duplicates(numbers)
print(f"duplicate numbers is : {result}")
