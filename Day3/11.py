def prime(n):
    if n > 1:
        for i in range (2,n):
            if n % i == 0:
                print('Number is not a Prime Number!!!')
                break
        else:
            print('Number is a prime Number!!!')
    else:
          print('Number is a prime Number!!!')
        
n = int(input('Enter the Value of Number:')) 
prime(n)
    
