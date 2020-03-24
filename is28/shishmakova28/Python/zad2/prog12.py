a=[]
M=4
N=4
K=int(input('Номер 1столбца='))
P=int(input('Номер 2столбца='))
print('введите массив')
for i in range(M):
	a.append([])
	for j in range (N):
		a[i].append(0)
for i in range(M):
	for j in range(N):
		a[i][j]=int(input())
print(a)
for i in range(M):
	t=a[i][K-1]
	a[i][K-1]=a[i][P-1]
	a[i][P-1]=t
print(a)
		

