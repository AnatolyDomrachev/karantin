def vvod():
	a=[]
	for i in range(n):
		a.append(int(input()))
	return a

def raschet(a):
	e=a[0]
	for i in range(1,n):
		if e<a[i]:
			e=a[i]
	y=a[0]
	for i in range(1,n):
		if y>a[i]:
			y=a[i]
	c = e-y  
	
	
	
def vyvod(c):	
	print("Ответ: ", c)
	
	
	
n=int(input())	
a=vvod()
c=raschet(a)
vyvod(c)
	