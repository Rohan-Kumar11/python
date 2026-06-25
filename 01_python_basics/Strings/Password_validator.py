str = input("Enter the password : ")
has_upper=False
has_lower=False
has_digit=False
has_special=False
special = "!@#$%^&*"
if len(str)<13 and len(str)>8 and " " not in str:
    for char in str :
        if char.isupper():
            has_upper=True
        elif char.islower():
            has_lower=True
        elif char.isdigit():
            has_digit=True
        elif char in special:
            has_special=True
    if has_special and has_digit and has_lower and has_upper:
        print("The password is valid.")
    else:
        print("The password is not valid.")
else:
    print("The password length should be greater than 8 and less than 13.")