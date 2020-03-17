def vvod():
 f=open('mass.txt','r')
 a=[]
 v = {}
 for i in range(2):
  p=f.readline()
  p1=p.split(':')
  v['name']=p1[0]
  v['grp']=p1[1]
  v['age']=int(p1[2])
  a.append(v.copy())
 f.close()
 return a
 
def dob():
 y={}
 y['name']=str(input('Введите имя:'))
 y['grp'] =input('Введите грyппy:')
 y['age']=int(input('Введите возраст:'))
 return y
 
def res(a,y):
 a.append(y)
 f=open('mass.txt','w')
 for y in a:
  print(y['name']+':'+y['grp']+':'+str(y['age'],file=f)

a=vvod()
y=dob()
vyvod=res(a,y)
