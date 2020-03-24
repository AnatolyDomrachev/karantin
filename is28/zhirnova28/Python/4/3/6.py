import math
x=int(input("Введите номер дня в годy:"))
y=x+1//7
print(not bool(y%2==0 or (x%7==0 and y%2==0)))
