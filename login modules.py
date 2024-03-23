self.uname=uname
self.pwd=password
self.phonenumber=phonenumber
with open('login details.csv','a',newlines='') as file:
    store=csv.write(file)
    store.writerow(self.uname,self.pwd,self.phonenumber)
def login(self,uname,password):
    with open('login details.csv','r',newlines='') as file:
        read = csv.dictread(file)
        for row in read:
            if (row[uname]==uname and row[pwd]==password):
                 print("the login is successfull")
            else:
                print("invalid credinitals")