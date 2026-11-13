sentence = input("Enter a sentence: ")
words = sentence.split()
shortest_word = words[0]

for word in words:
    if len(word) < len(shortest_word):
        shortest_word = word

print(f"The shortest word in the sentence is: {shortest_word}")