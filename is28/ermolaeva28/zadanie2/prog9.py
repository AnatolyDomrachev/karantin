a = []
m=4
n=4
for i in range(m):
	a.append([])
	for j in range(n):
		a[i].append(int(input()))
print(a)
e=a[0][0]
k=0
y=0
for i in range(0,n):
	for j in range(0,n):
		if e<a[i][j]:
			e=a[i][j]
			k=i
			y=j
	print("Наиб. значение =", e, "Строка = ", k+1, "Столбец =", y+1)