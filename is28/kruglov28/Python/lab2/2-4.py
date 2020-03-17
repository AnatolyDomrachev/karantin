import math
rv = float(input("Введите угол, значения синуса и косинуса которого хотите получить - "))
r = math.radians(rv)
sinr = math.sin(r)*10//1/10
cosr = math.cos(r)*10//1/10
print("Синус введённого угла равен",sinr, '\n' "Косинус введённого угла равен",cosr)
