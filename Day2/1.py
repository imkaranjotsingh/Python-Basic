r = 0
n = 1283
while n >= 1:
    r = r * 10 + n % 10
    n = n // 10
print(r)
