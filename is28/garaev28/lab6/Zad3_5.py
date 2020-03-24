import random

def arrayent(a):
    for i in range (0,5):
        a[i]=int(random.randint(-10,10))
        #a[i]=float(input())
    return a

def arrayprt(a):
    for i in range (0,5):
        print(a[i])

def repchk(a):
    ok=bool(0)
    for i in range (0,4):
        for j in range (i+1,5):
            if a[i]==a[j]:
                ok=bool(1)
    return ok

x=[0,0,0,0,0]
arrayent(x)
arrayprt(x)
if repchk(x)==1:
    print ('Есть повторы')
else:
    print('Повторов нет')
