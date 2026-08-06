

len = int(input("Enter the length of the pattern : "))

'''
1
12
123
1234
12345
'''
print("1. Increasing Number Triangle")
for i in range(1,len+1):
    for j in range(1,i+1):
        print(j,end="")
    print("\n")
    
'''
12345
1234
123
12
1
'''
print("2. Decreasing Number Triangle")
for i in range(1, len+1):
    for j in range(1,len-i+2):
        print(j,end="")
    print("\n")
    
    
'''
1
22
333
4444
55555
'''
print("3. Same Number Triangle")
for i in range(1,len+1):
    for j in range(1,i+1):
        print(i,end="")
    print("\n")
    
'''
55555
4444
333
22
1
'''

print("4. Reverse Same Number Triangle")
for i in range(1, len+1):
    for j in range(1,len-i+2):
        print(len+1-i,end="")
    print("\n")
    
'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
'''
print("5. Floyd's Triangle")
count=1
for i in range(1,len+1):
    for j in range(1,i+1):
        print(count,end=" ")
        count+=1
    print("\n")
    
'''
15
14 13
12 11 10
9 8 7 6
5 4 3 2 1
'''

print("6. Reverse Floyd's Triangle")
count = int((len**2)/2)+3
for i in range(1,len+1):
    for j in range(1,i+1):
        print(count,end=" ")
        count-=1
    print("\n")