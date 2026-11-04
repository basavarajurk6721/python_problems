text = input("Enter a string: ")

reverse = ""

for char in text:
    reverse = char + reverse

if text == reverse:
    print(f"The string '{text}' is a palindrome")
else:
    print(f"The string '{text}' is not a palindrome")