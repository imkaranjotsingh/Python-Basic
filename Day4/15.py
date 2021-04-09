from array import *
a = array('i',[1,2,3,4,5,6,7,0,0,0,0,0,0,0])
i = 0
c = len(a)
for i in range(1 , 13, 2 ):
    for j in range(12 ,i ,-1):
        a[j+1] = a[j]
    a[i] = 7
for i in range(0 , 14 ,1):
    print(a[i])


    
