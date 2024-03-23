mytuple=("kareem","RCB","CSK","PAUL","PILI",1,2,3,5)
print(type(mytuple))
# ading the values
mytuple=mytuple+("friyaa",)
print(mytuple)
#add multiple values
mytuple=mytuple+(12,3.25,"friyaa")
print(mytuple)

# for lop in tuple
for i in range(0,3):
    n=int(input("enter the value"))
    mytuple=mytuple+(n,)
print(mytuple)