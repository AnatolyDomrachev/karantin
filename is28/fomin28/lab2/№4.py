ugol=float(input("Введите угол: "))
import math
ugol=(ugol * math.pi)/180
cos=math.cos(ugol)
sin=math.sin(ugol)
print("Синус угла =%.2f"%(sin),"Косинус угла =%.2f"%(cos))
