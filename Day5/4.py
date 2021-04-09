class student:
    def set(self , n ,r):
        self.name = n
        self.rollno = r
    def show(self):
        print(self.name)
        print(self.rollno)

class result(student):
    def setr(self,m):
        self.marks = m
    def show(self):
        print(self.marks)
        super().show()
r1 = result()
r1.set('ajay',100)
r1.setr(120)
r1.show()
