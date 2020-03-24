a=[]
print("Введите массив:")
for i in range (10):
	b=int(input());
	a.append(b)
print(a)
x=int(input("Введите х:"))
y=0
for i in range (10):
	if a[i]==x:
		y=y+1
if y>0:
	print('True')
