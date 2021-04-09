class fees:
    def set(self):
        self.cource = input('Enter the Name of cource:')
        self.fee = int(input('Enter the fees :'))
    def show(self):
        print(self.cource)
        print(self.fee)

abc = list(range(7))

#print(abc[-1])
i = 0
for i in range(0 , 5 ,1):
    abc[i] = fees()
    abc[i].set()
    if(abc[i].fee>2000):
        abc[i].show()
    
