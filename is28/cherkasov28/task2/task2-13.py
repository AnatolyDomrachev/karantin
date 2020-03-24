import random

size = 4

def swapStrings(matrix,j,k):
    for i in range(0,size):
        matrix[j][i], matrix[k][i] = matrix[k][i], matrix[j][i]

def printMatrix(matrix):
    print()
    for element in matrix:
        print('{:5}\t{:5}\t{:5}\t{:5}'.format(*element)) 
    print()

def getIndexOfMinOfFirstColonum(matrix):
    elementFromFirstColonum = [ matrix[i][0] for i in range(0,size) ]
    return elementFromFirstColonum.index(max(elementFromFirstColonum))


a = [ [random.randint(0,99999) for j in range(0,size)] for i in range(0,size) ]

print("Изначальная матрица:\n")
printMatrix(a)

swapStrings(a,0,getIndexOfMinOfFirstColonum(a))

print("Измененная матрица:\n")
printMatrix(a)