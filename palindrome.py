n =1441
ans=0
while n>0:
    digit=n%10
    ans=ans*10+digit
    n=n//10
 print(ans)