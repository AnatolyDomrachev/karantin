an=[]
print("Введите данные массива")
for i in range(10):
 x=int(input())
 an.append(x)
i=int(input("Введите число, для которого необходимо найти количество одинаковых элементов "))
if an.count(i)==1:
 print("Нет одинаковых элементов")
else:
 print("Количество одинаковых элементов:",an.count(i))
if an.count(i)==0:
 print("Данный элемент отсyтствyет в массиве")