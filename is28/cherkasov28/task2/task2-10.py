import random

size = 4

def getMin(matrix):
    return  min([ min(matrix[i]) for i in range(0,size) ])
    
def getMax(matrix):
    return max([ max(matrix[i]) for i in range(0,size) ])

def printMatrix(matrix):
    print()
    for element in matrix:
        print('{:5}\t{:5}\t{:5}\t{:5}'.format(*element)) 
    print()


a = [ [random.randint(0,99999) for j in range(0,size)] for i in range(0,size) ]

printMatrix(a)
print("Разница между максимальным и минимальным элементами = ",getMax(a) - getMin(a))