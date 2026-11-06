text = input("Enter a string: ")

reverse = ""

for char in text:
    reverse = char + reverse

if text == reverse:
    print("True")
else:
    print("False")