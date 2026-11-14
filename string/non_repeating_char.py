text = str(input("Enter a string: "))

for char in text:
    if text.count(char) == 1:
        print(f"The first non-repeating character in the string '{text}' is '{char}'")
        break
else:
    print(f"There are no non-repeating characters in the string '{text}'")