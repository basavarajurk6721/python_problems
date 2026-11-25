def find_longest_word(sentance):
    words = sentance.split()
    largest = ""

    for word in words:
        if len(word) > len(largest):
            largest = word
    return largest
text = input("Enter a string :")
result = find_longest_word(text)
print(f"largest word is : {result}")