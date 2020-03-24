def dataRead(pathway):
    try:
        with open(pathway) as file:
            arrays = [ list( map(float,(file.readline()).split() ) ) for i in range(0,3) ]
            # for i in range(0,3):
            #     content = file.readline()
            #
            #     if not content:
            #         print("Ошибка! Заданы не все входные данные")
            #         exit()
            #  
            #     arrays.append( list( map(float,content) ) )
                
    except FileNotFoundError:
        print("Ошибка! Файл с таким названием не существует.")
        exit()

    except ValueError:
        print("Ошибка! Некорректный формат данных.")
        exit()

    else:
        return arrays[0],arrays[1],arrays[2]


def dataOutput(pathway,arr):
    with open(pathway,'w') as file:
        file.write("Массив с наименьшим значением: "+ str(arr))


def findArrayWithMinimalElement(x,y,z):
    # try:
        minElement = min( [min(x),min(y),min(z)] )
    # except:
    #     print("Ошибка! Заданы не все входные данные")
    #     exit()
    
    return (x if minElement == min(x) else (y if minElement == min(y) else z ))

x,y,z = dataRead("data.txt")
arr = findArrayWithMinimalElement(x,y,z)
dataOutput("result.txt",arr)
