  
N = int(input('Введите N: '))
 
for k in range(2, N+1):
 
    prime = True
    
    for i in range(2, k):
        if k%i == 0:
            prime = False
            break
 
    if prime == True :
        print('{} - простое число'.format(k))
    
