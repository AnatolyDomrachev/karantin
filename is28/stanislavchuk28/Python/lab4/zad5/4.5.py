def vvod_dannyh():
	n = open('test.txt','r')
	a=[]
	for i in range(0,10):
		a.append(float(n.readline()))
		n.close();
	return a
def ras(a):
	for i in range(1,len(a)):
		if a[i-1]<a[i]:
			return True
		else:
			return False
def vyvod(result):
	f=open('res.txt','w')
	print(result, file = f)
	f.close();
  
#главный модуль 
dannye = vvod_dannyh()
result=ras(dannye)
vyvod(result)
