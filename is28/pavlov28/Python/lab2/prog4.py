import math
grad = float(input("Градóсы = "))
grad = math.radians(grad)
sin = math.sin(grad)
cos = math.cos(grad)
print("%.1f" % (sin))
print("%.1f" % (cos))
