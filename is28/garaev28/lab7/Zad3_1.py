def datain (a):
 for i in range(0,5):
  a[i]=int(input())
 return a
 
def dataout (a):
 for i in range (0,5):
  print(a[i])

def sort (a):
 for i in range (0,4):
  for j in range (i,5):
   if a[i]<a[j]:
    r=a[j]
    a[j]=a[i]
    a[i]=r
 return(a)
    
 
b=[0,0,0,0,0]
datain(b)
sort(b)
dataout(b)
