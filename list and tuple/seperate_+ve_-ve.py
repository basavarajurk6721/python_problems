numbers = [10, -5, 20, -8, 0, 15, -3, 7]

positve = []
negative = []

for num in numbers:
    if num > 0:
        positve.append(num)
    elif num < 0:
        negative.append(num)

print("positve numbers",positve)
print("nagative number",negative)