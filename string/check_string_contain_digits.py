text = input("Enter a string: ")

if text == "":
    print("The string is not contain only digits.")
else:
    for char in text:
        if char < '0' or char > '9':
            print("The string is not contain only digits.")
            break
    else:
        print("The string is contain only digits.") 