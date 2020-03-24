m=4
n=4

def vvod(): 
	a=[]
	for i in range(m):
		a.append([])
		for j in range(n):
			a[i].append(int(input()))
	return a


def raschet(a):
	e=a[0][0]
	k=0
	y=0
	for i in range(0,n):
		for j in range(0,n):
			if e<a[i][j]:
				e=a[i][j]
				k=i
				y=j
	b=[]
	b.append(e)
	b.append(k)
	b.append(y)
	return b
	
def vyvod(a):
	print(a)




matrix = vvod()
bce = raschet(matrix)
vyvod(bce)