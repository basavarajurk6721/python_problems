text = input("Enter a string: ")
count = 0

for char in text:
    if char.lower() in 'aeiou':
        count += 1

print(f"The number of vowels in the string '{text}' is {count}")