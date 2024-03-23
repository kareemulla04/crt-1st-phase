def is_prime():
    f=1
    n=int(input("enter the value",))
    for i in range(2,n):
        if n%i==0:
           f=0
           break
    if f==1:
        print("the number is  prime")
    else:
        print("the number is not prime")
is_prime()