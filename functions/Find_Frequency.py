def Find_Frequency(numbers):
    frequency = {}

    for num in numbers:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    return frequency
numbers =input("Enter a number: ").split()
result = Find_Frequency(numbers)
for num, count in result.items():
    print(f"{num} occurs {count} times")