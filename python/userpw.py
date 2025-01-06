user_pwd="abcd123"

while(1):
    a=input("Enter password:")
    if(user_pwd!=a):
        print("Enter correct password:")
    else:
        print("")
        print("Password is correct")