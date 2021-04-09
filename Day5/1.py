class student:
    def set(self , name , rollno):
        self.name = name
        self.rollno = rollno
    def show(self):
        print(self.name , "  " ,self.rollno)

abc = student()
abc.set('ajay',100)
abc.show()
