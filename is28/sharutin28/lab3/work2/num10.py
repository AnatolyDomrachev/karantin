import random 
b = []
c = []
d = []
f = []
a = [b, c, d, f]
min = 100
max = 0
for i in range(4):
	x = random.randint(0, 100)
	b.append(x)
	if x<=min:
		min=x
	if x>=max:
		max=x
for i in range(4):
	x = random.randint(0, 100)
	c.append(x)
	if x<=min:
		min=x
	if x>=max:
		max=x
for i in range(4):
	x = random.randint(0, 100)
	d.append(x)
	if x<=min:
		min=x
	if x>=max:
		max=x
for i in range(4):
	x = random.randint(0, 100)
	f.append(x)
	if x<=min:
		min=x
	if x>=max:
		max=x
print(a)
print(max)
print(min)
print(max-min)