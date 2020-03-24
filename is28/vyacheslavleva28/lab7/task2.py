def vvod():
	v = []
	for i in range(10):
		x = int(input())
		v.append(x)
	return v

def raschet(v):
	x = int(input())
	
	nom = 0
	for i in range(len(v)):
		if v[i] == x:
			nom = i
	return nom

def vyvod(nom):
	if nom > 0:
		print(nom)
	else:
		print(-1)	

v = vvod()
print(v)
result = raschet(v)
print(result)
vyvod(result)