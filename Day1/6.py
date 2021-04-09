print('Enter the Marks of the Student')
a = int(input('Enter the marks of Maths:'))
b = int(input('Enter the marks of Biology:'))
c = int(input('Enter the marks of Physics:'))
avg = (a+b+c)/3
print('Average of 3 Subjects are',avg)
if avg >= 80 :
    print('A Grade')
elif avg >= 60 and avg <80:
    print('B Grade')
elif avg < 60 :
    print('Fail!!! Try Again!!!')
