text = str(input("Enter a string: "))
seen = ""
for char in text:
    if char in seen:
        print(f"the first repeated character in the string '{text}' is '{char}'")
        break
    seen += char
else:
    print(f"There are no repeated characters in the string '{text}'")