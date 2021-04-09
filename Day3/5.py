def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

n = int(input('Enter the Number:'))
if n < 0:
    print('Fact does not exist!!!')
elif n == 0:
    print('Fact of 0 is 1..')
else:
    print('Favtorial of ',n,'is',fact(n))

    
