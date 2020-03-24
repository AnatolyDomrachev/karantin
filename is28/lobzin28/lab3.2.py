import math
X=int(input("Введите число, трёхзначное:"))
a=X%10
b=X%100
c=b//10
d=X//100
print ("Сyмма цифр числа", d+c+a)