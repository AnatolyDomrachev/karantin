def vvod():
 a=str(input(''))
 return a
 
def kolich(str1):
 a=len(str1)
 return a
 
def raschet(str1):
 x=[]
 a=kolich(str1)
 for i in range(a):
  x.append(str1[i])
 return x
 
def probel(b):
 a=len(b)
 for i in range(a-1):
  if b[i]==b[i+1]==' ':
   b[i]=''
 return b

def massiv(b):
 for x in b:print(x,end='')
 print()
 
str1=vvod()
b=raschet(str1)
a=kolich(str1)
itog1=probel(b)
itog2=massiv(b)