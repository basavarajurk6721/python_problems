numbers = list(map(int, input("Enter numbers separated by space: ").split()))

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number
    elif number < smallest:
        smallest = number
print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")