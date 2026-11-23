def display_details(name, age, add):
    print(f"Name : {name}")
    print(f"age : {age}")
    print(f"add is : {add}")

name = input("Enter your name :")
age = input("Enter your age :")
add = input("Enter your add :")

result = display_details(name,age,add)
print(result)