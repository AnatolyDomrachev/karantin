a=[]
M=4
N=4
K=0
print('введите массив')
for i in range(M):
	a.append([])
	for j in range (N):
		a[i].append(0)
for i in range(M):
	for j in range(N):
		a[i][j]=int(input())
print(a)

for i in range(M-1):
	if a[i][0]<a[i+1][0]:
		K=K+1
print(K)
for j in range(N):
	c=a[0][j]
	a[0][j]=a[K][j]
	a[K][j]=c
print(a)
		