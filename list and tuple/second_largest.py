numbers = list(map(int, input("Enter numbers separated by space: ").split()))

largest = second_largest = float('-inf')
for number in numbers:
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest and number != largest:
        second_largest = number
if second_largest == float('-inf'):
    print("There is no second largest number in the list.")
else:
    print(f"The second largest number in the list is: {second_largest}")