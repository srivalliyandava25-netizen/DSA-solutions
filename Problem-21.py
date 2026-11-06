n = int(input("Enter a number: "))

total = 0

for i in range(1, n):
    if n % i == 0:
        total += i

if total == n and n > 0:
    print("True")
else:
    print("False")