'''
В матрице 4*4 поменяйте местами первую строку и строку, у которой первый элемент является
наибольшим среди элементов первого столбца.
'''

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
for i in range (4):
	print(a[i])



for i in range (4):
	if a[i][0] > max:
		max = a[i][0]
		index = i
'''
tmp = a[0]
a[0] = a[index]
a[index] = tmp
'''
a[0], a[index] = a[index], a[0]

print()
for i in range (4):
	print(a[i])




		