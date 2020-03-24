def vvod_dannyh():
	x=[]
	for i in range(6):
		x.append(int(input()))
	return x	
def raschet(x):	
	for i in range(len(x)):
		for j in range(i+1,len(x)):
			if x[j]<x[i]:
				x[j],x[i] = x[i],x[j]
	return x 
def vyvod_resultata(x):
	for i in range(6):
		print(x[i])
x = vvod_dannyh()
res = raschet(x)
vyvod_resultata(res)
	


	


	
		
	