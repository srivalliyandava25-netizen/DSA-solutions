text = input("Enter a string: ")

upper = 0
lower = 0
digits = 0
special = 0

for char in text:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
    elif char.isdigit():
        digits += 1
    else:
        special += 1

print("Upper:", upper)
print("Lower:", lower)
print("Digits:", digits)
print("Special:", special)