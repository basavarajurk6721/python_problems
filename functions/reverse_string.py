# def reverse_string(text):
#     reversed_text = ""

#     for char in text:
#         reversed_text = char + reversed_text
#     return reversed_text

# string = input("Enter a string: ")
# print("Reversed string:", reverse_string(string))



def reverse_string(text):
    reverse_text = text[::-1]
    return reverse_text

string =  input("Enter a string: ")
result = reverse_string(string)
print(f"result is : {result}")