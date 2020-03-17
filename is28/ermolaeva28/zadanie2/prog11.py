a = []
m=4
n=4
for i in range(m):
	a.append([])
	for j in range(n):
		a[i].append(int(input()))
print(a)
k=int(input())
l=int(input())
a[k], a[l] = a[l], a[k]
print(a)