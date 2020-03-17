a=[]
b=[]
M=4
N=4
for i in range(M):
	a.append([])
	for j in range(N):
		a[i].append(int(input()))
print(a)
for j in range(M):
	b.append([])
	for i in range(N):
		b[j].append(a[i][j])
print(b)
