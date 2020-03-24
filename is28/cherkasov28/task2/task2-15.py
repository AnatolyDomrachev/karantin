import random

size = 5

def printMatrix(matrix):
    print()
    for element in matrix:
        print('{:5}\t{:5}\t{:5}\t{:5}\t{:5}'.format(*element)) 
    print()

def getAllIndexOf(arr,value):
    indicesList = []
    curIndex = -1
    for i in range(0,arr.count(value)):
        indicesList.append(arr.index(value,curIndex+1))
        curIndex = indicesList[i]
    return indicesList


def getIndicesHighs(matrix):
    highs = {}
    for i in range(0,size):
        curMax = max(matrix[i])
        highs[i] = getAllIndexOf(matrix[i],curMax)
    return highs

def getIndicesLow(matrix):
    lows = {}
    for i in range(0,size):
        curMin = min(matrix[i])
        lows[i] = getAllIndexOf(matrix[i],curMin)
    return lows


def getIndicesHighsAndLow_columns(matrix):
    arr = []
    for i in range(0,size):
        arr.append( [ matrix[k][i] for k in range(0,size) ] )
    return getIndicesHighs(arr), getIndicesLow(arr)


def findSaddlePoints(maxStr,minStr,maxCol,minCol):
    for i in range(0,size):
        for j in range(0,len(maxStr[i])):
             for k in range(0,len(minCol[maxStr[i][j]])):
                if (i == ( minCol[ (maxStr[i])[j] ] )[k]):
                    print("Седловая точка: [{}][{}]".format((i+1),(maxStr[i][j]+1)))

        for j in range(0,len(minStr[i])):
            for k in range(0,len(maxCol[minStr[i][j]])):        
                if (i == ( maxCol[ (minStr[i]) [j] ] )[k]):
                    print("Седловая точка: [{}][{}]".format(i,maxStr[i][j]))
                    

a = [ [random.randint(0,99999) for j in range(0,size)] for i in range(0,size) ]
printMatrix(a)

maxStr = getIndicesHighs(a)
minStr = getIndicesLow(a)
maxCol, minCol = getIndicesHighsAndLow_columns(a)

findSaddlePoints(maxStr,minStr,maxCol,minCol)

