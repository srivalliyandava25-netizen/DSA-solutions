text = input("Enter an uppercase string: ")

result = ""

for char in text:
    if 'A' <= char <= 'Z':
        result += chr(ord(char) + 32)
    else:
        result += char

print("Lowercase:", result)