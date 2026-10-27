num = int(input("Enter the number to find the facitoral : "))
def fac(num):
    if num==0 or num==1:
        return 1
    else:
        return num*fac(num-1)
print(f"The factorical of {num} is {fac(num)}")