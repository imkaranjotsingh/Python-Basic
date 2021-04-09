from array import array
#new array
a = array('i')

a.append(100)
a.append(200)
a.append(300)

a.insert(1,900)

a.remove(200)

k = a.count(900)
print(k)

print(a)
