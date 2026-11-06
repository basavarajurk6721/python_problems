numbers = list(map(int, input("Enter numbers separated by space: ").split()))
even_numbers_loop = []
for num in numbers:
    if num % 2 == 0:
        even_numbers_loop.append(num)
print("Even numbers using loop:", even_numbers_loop)

# Using list comprehension
even_numbers_comprehension = [num for num in numbers if num % 2 == 0]
print("Even numbers using list comprehension:", even_numbers_comprehension)