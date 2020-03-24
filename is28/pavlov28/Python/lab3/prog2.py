import math
x = int(input("x = "))
y = x % 10
x = x // 10
z = x % 10
x = x // 10
x = x % 10
x = x + y + z
print(x)
