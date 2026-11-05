text = str(input("Enter a string: "))

text = text.strip()
text = text.lower()
print(f"modified string: {text}")

words = text.split()
for word in words:
    print(word)