d={104:"a",
   105:"s",
   106:"i",
   108:"w",
   109:"f"}
print(d)
#adding values
d[102]="asdf"
print(d)
#change the values
d[106]="qwer"
print(d)
#accessing the value
print(d[106])
#print keys
for i in d:
    print(i)
#print the values
for i in d.values():
    print(i)
#both keys and values
for x,y in d.items():
    print(x,y)
#remove key and value
d.pop(106)
print(d)


