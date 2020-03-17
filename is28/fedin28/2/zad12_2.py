def prtinMatrix(matrix):
	for i in range(0,4):
		print(matrix[i])
		
matrix = []
for i in range(0,4):
	matrix.append([ ])
	for j in range(0,4):
		el = input()
		matrix[i].append(el)
j = input()
k = input()
for i in range(0,4):
	temp = matrix[i][j] 
	matrix[i][j] = matrix[i][k]
	matrix[i][k] = temp
	# matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]