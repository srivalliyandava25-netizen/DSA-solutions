base = int(input())
exponent = int(input())
total = 1
for i in range(exponent):
    total *= base
print(total)