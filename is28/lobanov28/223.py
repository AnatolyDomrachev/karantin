def vvod_dannyh():
	x=[]
	y=[]
	z=[]
	for i in range(5):
		x.append(float(input()))
		y.append(float(input())) 
		z.append(float(input()))
	m=x[0]
	m1=y[0]
	m2=z[0]
	return x, y, z
def raschet(x, y, z):
	for i in range(5):
		if x[i]<m:
			m=x[i];
	for k in range(5):
		if y[k]<m1:
			m1=y[k]
	for j in range(5):
		if z[j]<m2:
			m2=z[j]
	return x, y, z
def vyvod_dannyh()
	mx=m
	if m>m1 and m>m2:
		mx=m
	if m1>m and m1>m2:
		mx=m1
	if m2>m1 and m2>m:
		mx=m2
	print(mx)

