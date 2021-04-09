n = [2,4,5,55,55,66]
i = 0
for i in range(2,6-1,1):
    n[i] = n[i+1]

n[5]=0
print(n)
