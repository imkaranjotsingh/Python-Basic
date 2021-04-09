class book:
    def set(self,bname,price):
        self.bname = bname
        self.price = price
    def output(self):
        print('--About Book--')
        print(self.bname)
        print(self.price)

class author(book):
    def set1(self,oname):
        self.oname = oname
    def output(self):
        print('--About Author--')
        print(self.oname)
        super().output()
        
class publish(author):
    def set2(self , pname,loc):
        self.pname = pname
        self.loc = loc
    def output(self):
        print('--Publisher Imformation--')
        print(self.pname)
        print(self.loc)
        super().output()
        
class customer(publish):
    def set3(self , name , phone):
        self.name = name
        self.phone = phone
    def output(self):
        print('--Customer Name--')
        print(self.name)
        print(self.phone)
        super().output()

obj = customer()
obj.set('Fault in Our Stars!!!',700)
obj.set1('Jhon Green')
obj.set2('ABC house','Chandigarh')
obj.set3('Ajay',9876543210)
obj.output()

    
    
