x = []
summ = 0
n = int( input("Введите число элеметнов массива ") )
for i in range(n):
	x.append(int(input("введите элемент массива ")))
for i in range(n):
	summ = summ + x[i]
print(summ/n)
