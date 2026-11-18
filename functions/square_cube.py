def square_cube(num):
    square = num ** 2
    cube = num ** 3

    return square,cube
num = int(input("Enter a number "))
s,c = square_cube(num)
print(f"{num} square is {s}")
print(f"{num} cube is {c}")