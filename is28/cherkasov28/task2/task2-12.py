import random

size = 4

def swapColumns(matrix,j,k):
    for i in range(0,size):
        matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]

def printMatrix(matrix):
    print()
    for element in matrix:
        print('{:5}\t{:5}\t{:5}\t{:5}'.format(*element)) 
    print()


a = [ [random.randint(0,99999) for j in range(0,size)] for i in range(0,size) ]
printMatrix(a)

j,k = map(int,input("Введите числа j и k: ").split())
swapStrings(a,j-1,k-1)
printMatrix(a)
