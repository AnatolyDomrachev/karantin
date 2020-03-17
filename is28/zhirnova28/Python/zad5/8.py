def vvod():
 f=open('data.txt','r')
 x=[]
 for i in range(10):
  y=int(f.readline())
  x.append(y)
 return x
 
def raschet():
 n=0
 for i in range(0,len(x)-1):
  if ((x[i-1]<x[i] and x[i+1]<x[i] or x[i-1]>x[i] and x[i+1]>x[i])): 
   n+=1
 return n
 
def vyvod_resultata(x):
 f=open('res.txt','w')
 print("Количество поворотных точек равно: ",n,file=f)
 

x=vvod()
n=raschet()
vyvod_resultata(x)
