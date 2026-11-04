text = input("Enter a string: ")

reverse = ""
for char in text:
    reverse = char + reverse

print(f"The reverse of the string '{text}' is '{reverse}'")