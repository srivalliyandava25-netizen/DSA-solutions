n = int(input())
last = n % 10
while n >= 10:
    n //= 10
first = n
print("first:", first, "last:", last)