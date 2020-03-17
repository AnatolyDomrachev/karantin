import random
x={}
y={}
z={}
a=float(1000000)
b=int(0)

for i in range(0,5):
 x[i]=float(input())
 if x[i]<a:
  a=x[i]
  b=1
 
for i in range(0,5):
 y[i]=float(input())
 if y[i]<a:
  a=y[i]
  b=2
   
for i in range(0,5):
 z[i]=float(input())
 if z[i]<a:
  a=z[i]
  b=3 

if b==1:
 for i in range (0,5):
  print (x[i])
elif b==2:
 for i in range (0,5):
  print (y[i])
else:
 for i in range (0,5):
  print (z[i])