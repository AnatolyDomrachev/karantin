def readData(pathway):
    dictArr = []

    try:
        with open(pathway) as file:
            for line in file:
                key, *val = line.split()
                dictArr.append({}.fromkeys(key,val))

            if not file:
                print("Ошибка! Заданы не все данные.")
                exit()

    except FileNotFoundError:
        print("Ошибка! Файл с таким названием не существует.")
        exit()

    except ValueError:
        print("Ошибка! Некорректный формат данных.")
        exit()
    else:
        return dictArr


pathway = "data.txt"
dictArr = readData(pathway)
for dictionary in dictArr:
    print(dictionary)