class employee:
    def setemp(self , em ,m, sal):
        self.empno = em
        self.name = m
        self.salary = sal
    def show(self):
        print(self.empno)
        print(self.name)
        print(self.salary)

obj = employee()
obj.setemp(100,'ajay',20000)
obj2 = employee()
obj2.setemp(101,'Vijay',5000)

if obj.salary > obj2.salary:
    obj.show()
else:
    obj2.show()

    
        
