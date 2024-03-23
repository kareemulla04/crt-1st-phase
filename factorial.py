n=47
sum=0
n1=n
while n1>0:
    d=n%10
    sum=sum+d
    n1=n1//10
print(sum)
if n%sum==0:
    print("divisible")
else :
    print("its not divisible")
