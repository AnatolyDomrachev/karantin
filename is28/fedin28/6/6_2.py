def dictWithStr(dictArr,searchedStr):
    if not searchedStr:
        for dictionary in dictArr:
            print(dictionary)
        return

    for dictionary in dictArr:
        if dictionary.setdefault(searchedStr):
            print(dictionary)


dictArr = [ {'013':[1,2,3]},
    {'wye':[0,9,3]},
    {'beb':[2,4,6]},
    {'013':['wwewe',3,'hi']} ]

searchedStr = input("Введите строку, по которой будет осуществляться поиск:\n")
dictWithStr(dictArr,searchedStr)