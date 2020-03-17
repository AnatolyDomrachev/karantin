def mySort(arr,k):
    for i in range(k+1,len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i]>arr[j]):
                arr[i], arr[j] = arr[j], arr[i]       


x = [1,2,9,7,6,5]

k = int(input("Введите k: "))
mySort(x,k)
print("Отсортированный массив: ",x)
