import random

def arrayent(a,n):
 if n==1:
  f=open('Input2_1.txt','r')
 elif n==2:
  f=open('Input2_2.txt','r')
 elif n==3:
  f=open('Input2_3.txt','r')

 for i in range (0,5):
  n=float(f.readline())
  a[i]=n
  #a[i]=float(random.uniform(-999,999))
  #a[i]=float(input())
 f.close
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
 f=open('Output2.txt','w')
 if findmax(arraymin(a),arraymin(b),arraymin(c))==arraymin(a):
  print('Массив X')
  f.write(str('Массив X')+'\n')
  for i in range(0,5):
   print(a[i])
   f.write(str(a[i])+'\n')
 if findmax(arraymin(a),arraymin(b),arraymin(c))==arraymin(b):
  print('Массив Y')
  f.write(str('Массив Y')+'\n')
  for i in range(0,5):
   print(b[i])
   f.write(str(b[i])+'\n')
 if findmax(arraymin(a),arraymin(b),arraymin(c))==arraymin(c):
  print('Массив Z')
  f.write(str('Массив Z')+'\n')
  for i in range(0,5):
   print(c[i])
   f.write(str(c[i])+'\n')
 f.close



x=[0,0,0,0,0]
y=[0,0,0,0,0]
z=[0,0,0,0,0]
arrayent(x,1)
arrayent(y,2)
arrayent(z,3)
result(x,y,z)