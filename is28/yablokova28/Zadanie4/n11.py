def vvoda():
	a = input()
	return(a)

def vvodb():
	b = input()
	return(b)

def tomat(a,b):
	x = list(a)
	y = list(b)
	arr = []
	for i in range(len(x)):
		for j in range(len(y)):
			if x[i]==y[j]:
				arr.append(x[i])
	print(arr)		

a = vvoda()
b = vvodb()
tomat(a, b)	




