def dataInput():
    print("Введите элементы массива: ")
    return list(map(int,input("").split())), int(input("\nВведите k: "))

def mySort(arr,k):
    for i in range(k+1,len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]>arr[j]):
                arr[i], arr[j] = arr[j], arr[i]   

def printArray(arr):
    print(arr)

arr, k = dataInput()
mySort(arr,k)
printArray(arr)
