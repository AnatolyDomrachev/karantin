import random

def arrayent(a):
    for i in range (0,5):
        a[i]=float(random.uniform(-999,999))
        #a[i]=float(input())
    return a

def arraymin(a):
    amin=float(1000)
    for i in range (0,5):
        if a[i]<amin:
            amin=a[i]
    return amin

def findmax (a,b,c):
    amax=float(-1000)
    if a>amax:
        amax=a
    if b>amax:
        amax=b
    if c>amax:
        amax=c
    return amax
    
    
def result (a,b,c):
 if findmax(arraymin(a),arraymin(b),arraymin(c))==arraymin(a):
    print('Массив X')
    for i in range(0,5):
        print(x[i])
 if findmax(arraymin(a),arraymin(b),arraymin(c))==arraymin(b):
    print('Массив Y')
    for i in range(0,5):
        print(y[i])
 if findmax(arraymin(a),arraymin(b),arraymin(c))==arraymin(c):
    print('Массив Z')
    for i in range(0,5):
        print(z[i])

x=[0,0,0,0,0]
y=[0,0,0,0,0]
z=[0,0,0,0,0]
arrayent(x)
arrayent(y)
arrayent(z)
result(x,y,z)