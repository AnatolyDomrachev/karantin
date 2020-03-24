def readData(pathway):
    try:
        with open(pathway) as file:
            contents = file.readline()
            k = file.readline()

            if not contents or not k:
                print("Ошибка! Заданы не все данные.")
                exit()

    except FileNotFoundError:
        print("Ошибка! Файл с таким названием не существует.")
        exit()

    except ValueError:
        print("Ошибка! Некорректный формат данных.")
        exit()
    else:
        return list(map(int,contents.split())), int(k)

def mySort(arr,k):
    for i in range(k+1,len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]>arr[j]):
                arr[i], arr[j] = arr[j], arr[i]   

def outputData(arr,pathway):
    with open(pathway,'w') as file:
        file.write(str(arr))

arr, k = readData("data.txt")
mySort(arr,k)
outputData(arr,"result.txt")