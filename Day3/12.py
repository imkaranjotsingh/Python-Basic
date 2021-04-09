def even(a,b):
    i = 0
    for i in range (a , b+1):
        if a % 2 == 0:
            print(a)
        a = a + 1
    return a
            
a = int(input('Enter the Starting Number:'))
b = int(input('Enter the Ending Number:'))
output = even(a,b)  
print('Even no Between',a,'to',b ,'are:', output)
