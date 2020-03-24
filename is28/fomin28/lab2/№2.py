x1=float(input("введите х1"))
y1=float(input("введите у1"))
x2=float(input("введите х2"))
y2=float(input("введите у2"))
import math
distance=float(math.sqrt((x2-x1)**2 + (y2-y1)**2))
print("расстояние=%.3f" %(distance))
