def dictWithStr(dictArr,searchedStr):
    if not searchedStr:
        for dictionary in dictArr:
            print(dictionary)
        return

    for dictionary in dictArr:
        if dictionary.setdefault(searchedStr):
            print(dictionary)

dictArr = [ {'012':[1,2,3]},
    {'wwe':[0,9,3]},
    {'bbb':[2,4,6]},
    {'012':['wwewe',3,'hi']} ]
searchedStr = input("Введите строку, по которой будет осуществляться поиск:\n")
dictWithStr(dictArr,searchedStr)