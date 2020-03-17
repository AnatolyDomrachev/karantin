N=4
M=4
def read_matrix():
    print("Ввод матрицы:")
    m = []
    for i in range(M):
        m.append([])
        for j in range(N):
            m[i].append(int(input()))
    return m

def f_max_stl(m):
 mmax= m[0][0]
 jmax=0
 imax=0
 for i in range (4):
  if mmax<= m[i][0]:
    mmax=m[i][0]
    imax=i    
 return imax
   

def swap(m):
 imax=f_max_stl(matrix)
 matrix[0],matrix[imax] = matrix[imax],matrix[0]

#Главный модyль
matrix = read_matrix()

print("Старый массив:")
for i in range(M):
    print(matrix[i])
  
swap(matrix)

print("Измененный массив:")

for i in range(M):
    print()
    for j in range(N):
       print(matrix[i][j], "\t", end="")



