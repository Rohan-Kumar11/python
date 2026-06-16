str = input("Enter the string : ")
count=0;
for i in str.lower() :
    if i in 'aeiou':
        count+=1;
print(f"The string \'{str}\' contain {count} vowels.")