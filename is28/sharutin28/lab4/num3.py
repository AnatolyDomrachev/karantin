import random
n = int(input())
a = []
count = 0
for i in range(n):
	x = random.randint(0, 10)
	a.append(x)
v = int(input())
for i in range(n):
	if a[i] == v:
		count+=1
print(a)
print(count)