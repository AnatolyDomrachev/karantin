def vvod():
 a=str(input())
 return a
 
def simv(str1,str2):
 a=len(str1)
 b=len(str2)
 return a,b

def raschet(str1,str2):
 x=[]
 a,b=simv(str1,str2)
 for i in range(a):
  if str1[i] in str2:
   x.append(str1[i])
 return x
 
str1=vvod()
str2=vvod()
massiv=raschet(str1,str2)
print(massiv)