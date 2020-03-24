def vvod():
	a=[]
	for i in range(5):
		n=float(input())
		a.append(n)
	return a

def raschet(a):
	res=0
	x=int(input('Введите число x',))
	for i in range(5):
		if a[i]==x:res=res+1
	return res

def vyvod(res):
	print(res)








a=vvod()
res=raschet(a)
vyvod(res)