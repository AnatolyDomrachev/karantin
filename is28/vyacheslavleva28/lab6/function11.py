def vvod():
	
	a = []
	M=4
	N=4
	for i in range(M):
		a.append([])
		for j in range(N):
			a[i].append(0)

	for i in range(M):
		for j in range(N):
			a[i][j] = int(input())

	for i in range(M):
		for j in range(N):
			print(a[i][j], end = '\t')
		print()
		
		
	return a

def rachet(a):
	i = int(input())
	k = int(input())
	
	a[i],a[k] = a[k],a[i]
	
	return a
	
def vyvod(data):
	print(data)


data = vvod()
print(data)
result = rachet(data)
print(result)
vyvod(result)
