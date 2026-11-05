text = str(input("Enter a string: "))

count = 0
in_words = False

for char in text:
    if char != " " and not in_words:
        count += 1
        in_words = True
    elif char == " ":
        in_words = False

print(f"The string '{text}' contains {count} words.")