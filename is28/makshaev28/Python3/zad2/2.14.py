M=3
N=3
def read_matrix():
    print("Введите матрицу")
    m = []
    for i in range(M):
        m.append([])
        for j in range(N):
            m[i].append(int(input()))
    return m

def transp(matrix):
	for i in range(len(matrix)):
		for j in range(i,len(matrix)):
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
	
	


matrix=read_matrix()
for i in range(M):
    print(matrix[i])
    
thunartransp(matrix)
for i in range(M):
    print()
    for j in range(N):
       print(matrix[i][j], "\t", end="")		
	

