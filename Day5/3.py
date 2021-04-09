class bank:
    def set(self,ac,n,bal):
        self.account = ac
        self.name = n
        self.balance = bal
    def deposit(self,n):
        self.balance = self.balance + n
    def withdraw(self,n):
        if n > self.balance:
            print('Not Enough Balance!!!!!!')
        else:
            self.balance = self.balance - n
    def show(self):
        print(self.account)
        print(self.name)
        print(self.balance)

b1 = bank()
b1.set(1000,'ABC',4000)
b1.show()
b1.deposit(1200)
b1.show()
b1.withdraw(13000)
b1.show()
