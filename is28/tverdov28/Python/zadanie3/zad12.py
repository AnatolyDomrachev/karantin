def inputMatrix():
	a = []
	print("заполните матрицу")
	for i in range(4):
		a.append([])
		for j in range(4):
			print("Введите число (",i,":",j,")")
			a[i].append(int(input("")))
	return a

def swapColumns(a,k,l):
	for i in range(4): 
		a[i][k], a[i][l] = a[i][l], a[i][k]


def printMatrix(a):
	for i in range(4):
 		print(a[i])

a = inputMatrix()
printMatrix(a)
print("Введите номера столбцов, которые нóжно поменять")
k, l = map(int,input("").split())
swapColumns(a,k,l)
printMatrix(a)
