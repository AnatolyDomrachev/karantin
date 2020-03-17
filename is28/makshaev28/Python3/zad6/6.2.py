def dictWithStr(dictArr,searchedStr):
    c=0
    for dictionary in dictArr:
        if searchedStr in dictionary:
            print(dictionary)
            c+=1
    if c==0:
        for dictionary in dictArr:
            print(dictionary)
    return
 
 
dictArr = [ {'013':[1,2,3]},
    {'wye':[0,9,3]},
    {'beb':[2,4,6]},
    {'013':['wwewe',3,'hi']} ]
 
searchedStr = input("Введите строку, по которой будет осуществляться поиск:\n")
dictWithStr(dictArr,searchedStr)

