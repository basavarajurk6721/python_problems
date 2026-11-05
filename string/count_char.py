text = str(input("Enter a string: "))
char = str(input("Enter a character to count: "))
count = 0

for ch in text:
    if ch == char:
        count += 1

print(f"The character '{char}' appears {count} times in the string '{text}'")