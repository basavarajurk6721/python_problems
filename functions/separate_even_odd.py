def separate_even_odd(numbers):
    even = []
    odd = []

    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even,odd
number = list(map(int,input("Enter the numbers : ").split()))
even_numbers,odd_numbers = separate_even_odd(number)
print(f"Even numbers is : {even_numbers}")
print(f"odd numbers is : {odd_numbers}")