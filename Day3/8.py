def sum(n):
    if n == 1 and n == 0:
        return n
    else:
        return n + sum(n-1)

    if n < 0:
        print('Enter the positive Number!!!!!!!!')

n = int(input('Enter the Numbers:'))
z = sum(n)
print('Sum is :', z)
        
