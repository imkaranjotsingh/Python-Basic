from abc import ABC, abstractmethod

class xyz(ABC):
    def show(self):
        pass
class xyz1(xyz):
    def show(self):
        print('Hello')
class xyz2(xyz):
    def show(self):
        print('Hello1')
class xyz3(xyz):
    def show(self):
        print('Hello2')
class xyz4(xyz):
    def show(self):
        print('Hello3')

R = xyz1()
R.show()

K = xyz2()
K.show()

R = xyz3()
R.show()

K = xyz4()
K.show()

