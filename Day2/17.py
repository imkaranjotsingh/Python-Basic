i = 0
k = 1
for i in range(1 , 6 , 1 ):
    for j in range( 1 , i+1 , 1):
        print(k , end = ' ')
        k = k + 1
    print('\r')
