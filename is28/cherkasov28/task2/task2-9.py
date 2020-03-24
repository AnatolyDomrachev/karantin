import random

size = 4

def printMatrix(matrix):
    print()
    for element in matrix:
        print('{:5}\t{:5}\t{:5}\t{:5}'.format(*element)) 
    print()

a = [ [random.randint(0,99999) for j in range(0,size)] for i in range(0,size) ]

maxElements = [ max(a[i]) for i in range(0,size)]
maxElement = max(maxElements)
maxElementIndex = maxElements.index(maxElement)

printMatrix(a)
print("\nМаксимальный элемент: ",maxElement,"\nСтрока: ",maxElementIndex+1,"\nСтолбец: ",a[maxElementIndex].index(maxElement)+1)