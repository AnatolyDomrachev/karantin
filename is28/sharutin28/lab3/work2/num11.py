import random 
b = []
c = []
d = []
f = []
a = [b, c, d, f]
k = int(input())
l = int(input())

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
	
print(a)
y = a[k]
a[k] = a[l]
a[l] = y
print(a)
