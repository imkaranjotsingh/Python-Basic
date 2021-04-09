class student:
    def set(self , name , rollno, physics, chemistry , maths):
        self.name = name
        self.rollno = rollno
        self.physics = physics
        self.chemistry = chemistry
        self.maths = maths
    def calculate(self):
        self.total = self.physics + self.chemistry + self.maths
        self.avg = self.total/3
        print('Total Marks:',self.total)
        print('Average :',self.avg)
        if self.avg >= 70:
            print('Grade is A')
        elif self.avg > 60 and self.avg < 70:
            print('Grade is B')
        else:
            print('Fail !!!!!')

obj = student()
obj.set('Ajay',100,88,89,77)
obj.calculate()
