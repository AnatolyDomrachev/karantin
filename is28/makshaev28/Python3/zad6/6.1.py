def readData(pathway):
 dictArr = []
 with open(pathway) as file:
  for line in file:
   key, *val = line.split()
   dictArr.append({}.fromkeys(key,val))
  return dictArr
 
 
pathway = "data.txt"
dictArr = readData(pathway)
for dictionary in dictArr:
    print(dictionary)
