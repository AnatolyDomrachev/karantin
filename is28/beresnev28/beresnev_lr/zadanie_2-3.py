a=[]
p=0
for n in range(10):
	k=int(input("Введите элемент массива = "))
	a.append(k)
t=int(input("Введи искомое число = "))
for l in range(10):
	if a[l] == t:
		p=p+1
if p == 0:
	print("В массиве нет этого число")
else:
	print("В массиве есть это число")