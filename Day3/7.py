def pow(n , p):
    if p :
        return n*pow(n,p-1)
    return 1
n = int(input('Enter the Base:'))
p = int(input('Enter the Power:'))
z = pow(n , p)
print('Output:',z)
