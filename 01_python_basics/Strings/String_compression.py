val= input("Enter the string : ").lower()  
value= "".join(sorted(val))
store=""
compression=""
if value == "":
    print("Empty string")

else:
    for char in value:
        if store == char :
            continue
        else:
            store= char
            compression+=char
            compression+=str(((value.rfind(char)-value.find(char))+1))
    print(compression)