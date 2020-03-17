def readData():
    dictionArr = []

    file = open('data.txt' , 'r')
   
    for line in file:
        key, *val = line.split()
        dictionArr.append({}.fromkeys(key,val))
    file.close()
    return dictionArr


dictionArr = readData()
for dictionary in dictionArr:
    print(dictionary)