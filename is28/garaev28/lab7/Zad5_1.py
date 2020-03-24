def datain (a):
 f=open('Input1.txt','r')
 for i in range(0,5):
  n=int(f.readline())
  a[i]=n
  #a[i]=int(input())
 f.close()
 return a
 
def dataout (a):
 f=open('Output1.txt','w')
 for i in range (0,5):
  f.write(str(a[i])+'\n')
  print(a[i])
 f.close()

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
