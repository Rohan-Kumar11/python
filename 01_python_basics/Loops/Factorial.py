n = int(input("Enter the number to find factorial : "))
fac=1
for i in range(n,1,-1):
    fac*=i
print(f"The factioral of {n} is {fac}")