import math 
x,y,x1,y1 = map(float,input("Введите координаты точек: ").split())
print("Расстояние между точками: ", math.sqrt(((x1-x)**2) + ((y1-y)**2)))