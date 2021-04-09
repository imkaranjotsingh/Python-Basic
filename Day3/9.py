def max(a,b,c):
    if a >= b and a >= c:
        if b >= c :
            return b
        else:
            return c
    elif b >= a and b >= c :
        if a >= c :
            return a
        else :
            return c
    elif a >= b :
        return a
    else:
        return b

a = int(input('Enter the value of A:'))
b = int(input('Enter the value of B:'))
c = int(input('Enter the value of C:'))
number = max(a,b,c)
print('Second largest Number is :',number)
