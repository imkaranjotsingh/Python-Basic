from array import *
a = array('i',[1,2,4,5,6,7,8,9,0])
c = len(a)
i = 0
for i in range(c-2 , 2-1 , -1):
    a[i + 1] = a[i]
a[2] = 3
print('Array after Insertion is :',a)
