str = (input("Enter the string : ")).lower()
if(str==(str[::-1])):
    print(f"The string \'{str}\' is palindrom.")
else:
    print(f"The string \'{str}\' is not palindrom.")