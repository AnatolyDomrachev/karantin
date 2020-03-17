def vvod_dannyh():
	x = int(input())
	v=[]
	for i in range(5):
		v.append(int(input()))
	return v, x

def raschet(v,x):	
	return v.count(x)
def vyvod_resultata(v):
	print(v)
v,x = vvod_dannyh()
res = raschet(v,x)
vyvod_resultata(res)