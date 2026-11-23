def calculate_average(*args):
    total = 0

    for num in args:
        total += num
    avarage = total/len(args)
    return avarage

result = calculate_average(10,20,30,40,50,60)
print(f"avarage is : {result}")