def readData():
    dictArr = []

    file = open('data.txt' , 'r')
    for line in file:
        key, *val = line.split()
        dictArr.append({}.fromkeys(key,val))
    file.close()
    return dictArr

def addDict(dictArr,dictionary):
    dictArr.append(dictionary)
    return dictArr

def writeData(dictArr):
    file = open('result.txt' , 'w')
    for dictionary in dictArr:
        file.write(str(dictionary)+'\n')
    file.close()
    return dictArr
            


dictArr = readData()
newDict = {'w':['dff',25,0]}
addDict(dictArr,newDict)
writeData(dictArr)


