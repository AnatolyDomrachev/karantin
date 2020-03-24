x=[]
y=[]
z=[]
print('Введите 1 массив')
for i in range(5):
	b=float(input())
	x.append(b)
print('Введите 2 массив')
for i in range(5):
	b=float(input())
	y.append(b)
print('Введите 3 массив')
for i in range(5):
	b=float(input())
	z.append(b)
if min(x)>min(y) and min(x)>min(z):print(x)
if min(y)>min(x) and min(y)>min(z):print(y)
else:print(z)

