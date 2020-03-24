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
 return a
 
def res():
 print(a)

a=vvod()
vyvod=res()

