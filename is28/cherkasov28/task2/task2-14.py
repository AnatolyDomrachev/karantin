import random

size = 4

def printMatrix(matrix):
    print()
    for element in matrix:
        print('{:5}\t{:5}\t{:5}\t{:5}'.format(*element)) 
    print()

def transposeMatrix(matrix):
    for i in range(0,size):
        for j in range(i,size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            

a = [ [random.randint(0,99999) for j in range(0,size)] for i in range(0,size) ]
printMatrix(a)

transposeMatrix(a)
printMatrix(a)