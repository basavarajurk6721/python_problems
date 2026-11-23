def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0

    for char in string:
        if char in vowels:
            count += 1
    return count
text = input("Enter a string : ")
result = count_vowels(text)
print(f"number of vowels is : {result}")