'''
*
**
***
****
*****
'''
print(" HALF PYRMAID")
height = int(input("Enter the height of the pyramid : "))
for i in range(1,height+1):
    for j in range(1,i+1,1):
        print(end="*")
    print("\n")

'''
*****
****
***
**
*
'''
print(" INVERTED HALF PYRMAID")
for i in range(1,height+1):
    for j in range(height-i,0,-1):
        print(end="*")
    print("\n")
    
'''
    *
   ***
  *****
 *******
*********
'''
print(" FULL PYRMAID ")
for i in range(1 , height+1):
    for j in range(height-i , 0 ,-1):
        print(end=" ")
    for j in range(1,i*2):
        print(end="*")
    print("\n")
    
'''
*********
 *******
  *****
   ***
    *
'''

print(" INVERTED FULL PYRMAID ")
for i in range(1, height+1):
    for j in range(1,i):
        print(end=" ")
    for j in range(1,(height+1-i)*2):
        print(end="*")
    print("\n")
    
'''
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
'''

print(" DIAMOND SHAPE")
for i in range(1 , height):
    for j in range(height-i , 0 ,-1):
        print(end=" ")
    for j in range(1,i*2):
        print(end="*")
    print("\n")
for i in range(1, height+1):
    for j in range(1,i):
        print(end=" ")
    for j in range(1,(height+1-i)*2):
        print(end="*")
    print("\n")