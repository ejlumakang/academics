# Create a user input that accept either string or number then detects if the string or number is a palindrome or not using conditional statement/loops.

user_input = input("Enter a string or number: ")
str = ''.join(user_input.split()).lower()

if str == str[::-1]:
    print("PALINDROME")
else:
    print("NOT PALINDROME")