def calculate_area(radius=5):
    area = 3.14 * radius ** 2
    return area

result1 = calculate_area()
print(f"area with difault radius : {result1}")

result2 = calculate_area(7)
print(f"area with radius 7 : {result2}")