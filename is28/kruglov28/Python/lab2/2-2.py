import math
x1 = int(input("Введите x1 точки A - "))
y1 = int(input("Введите y1 точки A - "))
x2 = int(input("Введите x2 точки B - "))
y2 = int(input("Введите y2 точки B - "))
if x1==x2 and y1==y2:
    print("Координаты обеих точек совпадают, описывая одну и ту же точку.")
    raise SystemExit
else:
    K1 = x1-x2
    K2 = y1-y2
    Dp = math.sqrt(K1**2+K2**2)
D = Dp//1 + (Dp-Dp//1)*1000//1/1000
print("Расстояние между точками A и B равно",D)
