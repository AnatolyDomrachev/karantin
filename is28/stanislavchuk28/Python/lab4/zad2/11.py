a=[]
M=4
N=4
for i in range (M):
	a.append([])
	for j in range (N):
		a[i].append(int(input()))
print(a)
m=int(input())
k=int(input())
for i in range (M):
	for j in range (N):
		c=a[k][j]
		a[k][j]=a[i][m]
		a[i][m]=c	
print(a)