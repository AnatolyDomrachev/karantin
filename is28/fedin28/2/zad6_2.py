import random
a = []
y = 0
b = int(input())
for i in range(b):
	x = random.randint(0,100)
	a.append (x)
	y +=x
y = float(y)
print(a)
print(y)
print(y/b)