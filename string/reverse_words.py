santance = str(input("Enter a sentence: "))
words = santance.split()
result = []

for word in words:
    reverse_word = " "
    for char in word:
        reverse_word = char + reverse_word
    result.append(reverse_word)
print("Reversed sentence:", " ".join(result))   