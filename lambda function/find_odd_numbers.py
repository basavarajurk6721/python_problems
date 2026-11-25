numbers = [10 ,15 ,20 ,25 ,30 ,35 ,40 ,45]
odd_numbers = list(filter(lambda num: num % 2 != 0, numbers))
print(f"original list",numbers)
print(f"odd numbers",odd_numbers)