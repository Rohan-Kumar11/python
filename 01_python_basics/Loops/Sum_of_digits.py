num = int(input("Enter the number to find its digits sum : "))
sum=0
while(num!=0):
    rem = int(num % 10)
    sum+=rem
    num =int(num/10)
print(f"The sum of number is {sum}")