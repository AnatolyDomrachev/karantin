n = int(input("Введите размерность массива: "))
a = []

for i in range(0,n):
    print("Введите ",i," элемент массива: ")
    temp = int(input())
    a.append(temp)

print("Среднее арифметическое всех элементов массива: ", sum(a)/len(a))
