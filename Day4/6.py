from array import *
a = array('i', [2,10,1,50,90,7,6])
z = a[0]
c = len(a)
i = 0
for i in range(i , c, 1):
    if a[i] > z:
        z = a[i]
print('Max No in array is :',z)
z = a[0]
i = 0
for i in range(i , c, 1):
    if a[i] < z:
        z = a[i]
print('Min No in array is :',z)
