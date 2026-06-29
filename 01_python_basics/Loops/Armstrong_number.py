n = int(input("Enter number: "))

power = len(str(n))

total = 0

for digit in str(n):
    total += int(digit) ** power

if total == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")