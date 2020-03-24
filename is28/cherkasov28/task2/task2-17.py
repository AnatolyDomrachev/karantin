import random

size = 4

def printMatrix(matrix):
    print()
    outputString = '{:5}\t'*len(matrix)
    for element in matrix:
        print(outputString.format(*element)) 
    print()

def replaceColumn(matrix,b,j):
    for i in range(0,size):
        matrix[i][j] = b[i]

a = [ [random.randint(0,99999) for j in range(0,size)] for i in range(0,size) ]
b = [ random.randint(0,99999) for i in range(0,size) ]

print("Матрица:")
printMatrix(a)
print("Вектор:\n\n",b,'\n')

j = int(input("Введите j: "))
replaceColumn(a,b,j-1)
printMatrix(a)