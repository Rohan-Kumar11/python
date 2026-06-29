n = int(input("Enter the number of terms : "))
a=0
b=1
print("Fibonacci Series : ",a,b,end=" ")
for i in range(n-2):
    sum=a+b
    print(sum ,end = " ")
    a=b
    b=sum
    