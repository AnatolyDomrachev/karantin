N=4
M=4
def read_matrix():
 f = open('data2.txt', 'r')
 m = []
 for i in range(M):
  m.append([])
  for j in range(N):
   n = int(f.readline())
   m[i].append(n)
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
 f=open('result2.txt','w') #открытие в режиме записи
 f.write(str(matrix))   # Запись  matrix в файл
 f.close
 




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



