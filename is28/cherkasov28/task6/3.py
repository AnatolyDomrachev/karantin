# def readData(pathway):
#     dictArr = []

#     try:
#         with open(pathway) as file:
#             for line in file:
#                 key, *val = line.split()
#                 dictArr.append({}.fromkeys(key,val))

#             if not file:
#                 print("Ошибка! Заданы не все данные.")
#                 exit()

#     except FileNotFoundError:
#         print("Ошибка! Файл с таким названием не существует.")
#         exit()

#     except ValueError:
#         print("Ошибка! Некорректный формат данных.")
#         exit()
#     else:
#         return dictArr

# def addDict(dictArr,dictionary):
#     dictArr.append(dictionary)

# def writeData(pathway,dictArr):
#     with open(pathway,'w') as file:
#         for dictionary in dictArr:
#             file.write(str(dictionary)+'\n')


# pathway = "data.txt"
# output = "result.txt"
# dictArr = readData(pathway)
# newDict = {0:[123,234,345]}
# addDict(dictArr,newDict)
# writeData(output,dictArr)


def addDict(pathway,dictionary):
    dictArr = []

    try:
        with open(pathway,'a') as file:
            file.write(str(dictionary)+'\n')
            

    except FileNotFoundError:
        print("Ошибка! Файл с таким названием не существует.")
        exit()

    except ValueError:
        print("Ошибка! Некорректный формат данных.")
        exit()
    else:
        return dictArr

pathway = "result.txt"
newDict = {0:[123,234,345]}
addDict(pathway,newDict)








