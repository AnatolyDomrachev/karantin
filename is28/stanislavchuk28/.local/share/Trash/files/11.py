a=[]
M=4
N=4
for i in range(M):
    a.append([])
    for j in range(N):
        a[i].append(int(input()))
print(a)
for i in range (M):
	for j in range(N):
		c=a[i][2]
		a[i][2]=a[4][j]
		a[4][j]=c
print(a)

