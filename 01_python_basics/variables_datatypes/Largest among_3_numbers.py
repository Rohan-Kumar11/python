num1=float(input("Enter the first number : "))
num2=float(input("Enter the second number : "))
num3=float(input("Enter the third number : "))
max=num1
if(max<num2 and num3<num2):
    max=num2
elif(max<num3 and num2<num3):
    max = num3
print(f"The largest number is {max}")