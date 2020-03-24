def findRepetitions(arr):
    for i in range(0,len(arr)):
       if(arr.count(arr[i])>1):
        return True
    return False


n = int(input("Введите размерность массива: "))
a = []

for i in range(0,n):
    print("Введите ",i," элемент массива: ")
    temp = int(input())
    a.append(temp)

print("Массив: \n\t",a,"\nЕсть ли повторения в массиве: ",findRepetitions(a))