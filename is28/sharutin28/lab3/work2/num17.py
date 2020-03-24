import random 
b = []
c = []
d = []
f = []
g = []
a = [b, c, d, f]
k = int(input())

for i in range(4):
	x = random.randint(0, 100)
	b.append(x)
	
for i in range(4):
	x = random.randint(0, 100)
	c.append(x)
	
for i in range(4):
	x = random.randint(0, 100)
	d.append(x)
	
for i in range(4):
	x = random.randint(0, 100)
	f.append(x)
	
for i in range(4):
	x = random.randint(0, 100)
	g.append(x)
print(a)
print(g)
a[k]=g
print(a)
