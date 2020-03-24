import random

size = 4

def getMatrixMinor(matrix,i,j):
    del matrix[i]
    for k in range(0,size-1):
        del matrix[k][j]

def printMatrix(matrix):
    print()
    outputString = '{:5}\t'*len(matrix)
    for element in matrix:
        print(outputString.format(*element)) 
    print()


a = [ [random.randint(0,99999) for j in range(0,size)] for i in range(0,size) ]
printMatrix(a)

i,j = map(int,input("Введите i и j: ").split())
getMatrixMinor(a,i-1,j-1)
printMatrix(a)
