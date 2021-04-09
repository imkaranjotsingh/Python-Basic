n = 1221
a = n
r = 0
while n >= 1:
    r = r * 10 + n % 10
    n = n // 10
print(r)
if r == a :
    print('The no is Palen!!!')
else:
    print('The no is not Palen!!!')
