def circule_area(radius):
    pi = 3.14
    area = pi * radius ** 2
    return area
r = int(input("Enter a radius :"))

if r < 0:
    print("Radius cannot be negative")
else:
    result = circule_area(r)
    print(f"area of circule is : {result}")