def vvod_dannyh():
	x=[]
	with open('data.txt') as a:
		x=[str(i) for i in a.read().split()]
	return x
def raschet(x):
	for i in range(6):
		for j in range(i+1, 6):
			if x[j]<x[i]:
				x[j],x[i]=x[i],x[j]
	return x
def vyvod_resultata(x):
		f1 = open("result.txt", 'w')
		for i in range(6):
			f1.write(x[i] )
		f1.close()
x = vvod_dannyh()
res= raschet(x)
vyvod_resultata(res)
