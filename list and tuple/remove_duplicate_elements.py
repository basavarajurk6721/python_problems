numbers = list(map(int, input("Enter numbers separated by space: ").split()))

unique_numbers = []
duplicate_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
    else:
        if number not in duplicate_numbers:
            duplicate_numbers.append(number)
unique_numbers.sort()
print(f"original list of numbers: {numbers}")
print(f"The list of unique numbers is: {unique_numbers}")
print(f"The list of duplicate numbers is: {duplicate_numbers}")
