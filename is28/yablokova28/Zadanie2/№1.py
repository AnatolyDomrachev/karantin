a=[]
for i in range(5):
    x=int(input())
    a.append(x)
print(a)

for i in range(len(a), 0, -1):
	for j in range(1, i):
		if a[j-1] > a[j]:
			n = a[j-1]
			a[j-1] = a[j]
			a[j] = n
print(a)	