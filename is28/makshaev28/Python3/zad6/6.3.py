def readData(pathway):
 dictArr = []
 with open(pathway) as file:
  for line in file:
      key, *val = line.split()
      dictArr.append({}.fromkeys(key,val))
 return dictArr
     
def addDict(dictArr,dictionary):
 dictArr.append(dictionary)

def writeData(pathway,dictArr):
 with open(pathway,'w') as file:
     for dictionary in dictArr:
         file.write(str(dictionary)+'\n')


pathway = "zad6.3.txt"
output = "result.txt"
dictArr = readData(pathway)
newDict = {3:["Vova",234]}
addDict(dictArr,newDict)
writeData(output,dictArr)
