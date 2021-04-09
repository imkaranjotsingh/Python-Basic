from array import *
a = array('i',[1,2,3,4,4,5,6,7])
c = len(a)
i = 0
for i in range(c-4 , c-1, 1 ):
    a[i] = a[i + 1] 
print('Array after deletion is:',a)
