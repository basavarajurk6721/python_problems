numbers = [10,15,20,25,30,35]
result = list(filter(lambda num : num % 2 == 0 , numbers))
print(f"original list is : {numbers}")
print(f"Even number is : {result}")