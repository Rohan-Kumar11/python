str = input("Enter a string: ")
print("The string is ",str)
l=[]
freq = {}

for char in str:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
for key,value in freq.items():
    if value > 1 :
        l.append(key)
print(l)