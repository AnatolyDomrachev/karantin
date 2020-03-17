A = [[1, 2, 3, 4], 
    [2, 4, 6, 8],
    [3, 6, 9, 12],
    [4, 8, 12, 16]]
i = int(input("Введите строку "))
j = int(input("Введите столбец "))
del A[i-1]
for k in range(len(A)):
	del A[k][j-1]
print("матрица 3x3 = ", A)