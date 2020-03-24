x = []
c=0
n = int( input("Введите количество элеметнов массива ") )
for i in range(n):
	x.append(int(input("введите элемент массива ")))
max = x[0]
min = x[1]
for i in range(len(x)):
	if x[i]>max:
		max=x[i]
for i in range(len(x)):
	if x[i]<min:
		min=x[i]
c = max-min
print("разница максимального и минимального элемента массива = ", c)
