num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []
for n in num:
    if n % 2 == 0:
        even_numbers.append(n)
print("numbers list",num)
print("Even numbers:", even_numbers)

# comprehension method
even_numbers = [n for n in num if n % 2 == 0]
print("Even numbers:", even_numbers)