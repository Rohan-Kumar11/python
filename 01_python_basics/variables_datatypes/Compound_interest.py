p = int(input("Enter the principal amount : ₹"))
r = float(input("Enter the interest rate (%) : "))
t = int(input("Enter the time in years : "))
n = float(input("Enter the number of times interest is compounded per year : "))

r = r / 100

A = p * pow((1 + r / n), n * t)

print("The compound interest is :", A - p)
print("Total amount is :", A)