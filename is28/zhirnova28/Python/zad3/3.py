def vvod_massiva():
 an=[]
 print("Введите данные массива")
 for i in range(10):
  x=int(input())
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
 print(res)

an=vvod_massiva()
i=vvod_chisla()
res=raschet(i)
vyvod=vyvod_resultata(res)
