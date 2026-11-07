text = input("Enter a string: ")

friquency = {}

for char in text:
    if char in friquency:
        friquency[char] += 1
    else:
        friquency[char] = 1

print(f"Character frequency in the given string: {friquency}")