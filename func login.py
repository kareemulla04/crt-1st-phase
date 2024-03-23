def login():
    n=1
    while n!=0:
        a=input("enter the username")
        b=input("enter the password ")   
        if a == b:
            print("you have login sucessfully")
            break
        else :
            print("invalid login")
login()
