import math
x = float(input("первая точка"))
y = float(input())
x1 = float(input("вторая точка"))
y1 = float(input())
k1 = x - x1
k2 = y - y1 
l= math.sqrt(k1* k1 + k2 * k2)
print ('%.3f' %l)