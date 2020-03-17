import math
x1 = float(input("Введите х1 "))
y1 = float(input("Введите y1 "))
x2 = float(input("Введите х2 "))
y2 = float(input("Введите y2 "))
s = (x1-x2)**2+(y1-y2)**2
s = math.sqrt(s)
s = round(s, 3)
print(s)