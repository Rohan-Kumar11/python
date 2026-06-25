str1 = input("Enter the first string : ").lower().replace(" ","")
str2 = input("Enter the Second string : ").lower().replace(" ","")
if sorted(str1) == sorted(str2):
    print("The string is Anagram.")
else:
    print("The string is not Anagram.")
    
# from collections import Counter
# str1 = input("Enter the first string : ").lower().replace(" ","")
# str2 = input("Enter the Second string : ").lower().replace(" ","")
# if counter(str1) == counter(str2):
#     print("The string is Anagram.")
# else:
#     print("The string is not Anagram.")
