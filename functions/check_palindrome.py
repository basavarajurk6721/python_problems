def check_palindrome(text):
    reversed_text = text[::-1]

    if text == reversed_text:
        return True
    else:
        return False
string = input("Enter a string :")
result = check_palindrome(string)

if result:
    print(f"{string} is a polindrome")
else:
    print(f"{string} is not a polindrom")