a=[]
M=4
N=4
for i in range (M):
	a.append([])
	for j in range (N):
		a[i].append(int(input()))
print(a)
for i in range (M):
	for j in range (N):
		b1=a[0][j]
		b2=a[1][j]
		b3=a[2][j]
		b4=a[3][j]
		c1=a[i][0]
		c2=a[i][1]
		c3=a[i][2]
		c4=a[i][3]
		a[0][j]=c1
		a[1][j]=c2
		a[2][j]=c3
		a[3][j]=c4
		a[i][0]=b1
		a[i][1]=b2
		a[i][2]=b3
		a[i][3]=b4
print(a)