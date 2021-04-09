a = int(input('Enter The value of A:'))
b = int(input('Enter the Value of B:'))
c = int(input('Enter the Value of C:'))
hcf = 1
i = 1
while i <= a:
    if a%i == 0 and b%i == 0 and c%i == 0:
        hcf = i
    i = i + 1
print(hcf)
