a=[]
M=3
N=3
for i in range(M):
    a.append([])
    for j in range(N):
        a[i].append(0)

print(a)

for i in range(M):
    for j in range(N):
        a[i][j] = int(input())

print(a)


