import random
b = []
c = []
d = []
f = []
a = [b, c, d, f]
max = 0
for i in range (4):
	x = random.randint(0, 100)
	b.append(x)
	
for i in range (4):
	x = random.randint(0, 100)
	c.append(x)
	
for i in range (4):
	x = random.randint(0, 100)
	d.append(x)
	
for i in range (4):
	x = random.randint(0, 100)
	f.append(x)
	
for i in range(4):
	for j in range(4):
		if a[i][j] > max:
			max = a[i][j]
			x = i+1 #строка
			y = j+1 #столбец

print(a)
print(max)
print(x, y) 
