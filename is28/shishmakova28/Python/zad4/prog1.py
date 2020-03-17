def vvod():
	a=[]
	for i in range(5):
		n=float(input())
		a.append(n)
	return a

def raschet(a):
	res=0
	x=int(input('Введите число x',))
	if a[0]==x:res=1
	else:res=-1
	return res

def vyvod(res):
	print(res)








a=vvod()
res=raschet(a)
vyvod(res)