def table(n ,q):
    r = 2
    if n <= q:
        r = r * n
        print(r)
        table( n + 1 ,q )
q = int(input('asas:'))
table(1,q)

