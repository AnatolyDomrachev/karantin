def vvod():
 f=open('mass.txt','r')
 a=[]
 v = {}
 for i in range(2):
  p=f.readline()
  p1=p.split(':')
  v['name']=p1[0]
  v['grp'] =p1[1]
  v['age'] =int(p1[2])
  a.append(v.copy())
 return a
  
def vvod_stroki():
 b=input('Введите строкy:')
 return b
 
def res(a,b):
 r=[]
 if b=='':
  return a
 for i in a:
  if b==i['name']:
   r.append(i)
  if b==i['grp']:
   r.append(i)
  if b==i['age']:
   r.append(i)
  return r
  
a=vvod()
b=vvod_stroki()
vyvod=res(a,b)
print(vyvod)