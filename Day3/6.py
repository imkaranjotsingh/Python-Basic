def fibb(n):
    if n <= 1:
        return n
    else :
        return fibb(n-1) + fibb(n-2)

n = int(input('Enter the Number:'))

if n <= 0:
    print('Please enter a Positive Integer!!!')
else:
    print('Fibb series is')
    for i in range(n):
        print(fibb(i))
