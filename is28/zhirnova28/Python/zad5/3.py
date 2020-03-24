def vvod_massiva():
 f=open('tri.txt','r')
 an=[]
 for i in range(10):
  x=int(f.readline())
  an.append(x)
 return an
  
def vvod_chisla():
 i=int(input("Введите число "))
 return i

def raschet(i):
 if i in an:
  res='TRUE'
 else:
  res='FALSE'
 return res
 
def vyvod_resultata(res):
 f=open('resu.txt','w')
 print(res,file=f)

an=vvod_massiva()
i=vvod_chisla()
res=raschet(i)
vyvod=vyvod_resultata(res)
