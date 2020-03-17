n = int(input("Введите размерность массива: "))
a = []

for i in range(0,n):
    print("Введите ",i," элемент массива: ")
    temp = int(input())
    a.append(temp)

print("Разность между наибольшим и наименьшим элементом массива: ",max(a)-min(a))