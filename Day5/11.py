/lass book:
    def set(self , author , publisher , bookname , price):
        self.outhor = author
        self.publisher = publisher
        self.bookname = bookname
        self.price = price
    #def cal(self ):

b1 = book()
b1.set('abc','xyz','qwe',150)
b2 = book()
b2.set('def','asd','azx',170)
b3 = book()
b3.set('gef','jsd','ezx',190)
b4 = book()
b4.set('wef','ksd','czx',120)
i = 0
a = []
a.append(b1.price)  
a.append(b2.price)
a.append(b3.price)
a.append(b4.price)
a.sort()
print('Second Highest Book is:')
print(a[1])
#print(self.author)
#print(self.publisher)
#print(self.bookname)
#print(self.price)
#print(a)
