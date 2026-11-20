def find_second_largest(numbers):
    largest = numbers[0]
    second_largest = None

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num < largest:
            if second_largest is None or num > second_largest:
                second_largest = num

    return second_largest
number = list(map(int, input("Enter numbers: ").split()))
result = find_second_largest(number)
if result is None:
    print("Second largest number does not exist")
else:
    print("Second largest number:", result)