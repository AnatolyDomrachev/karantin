a=b=1
n=int(input("Номер числа Фибоначчи:")) - 3
while n>0:
	a, b = b, a+b
	n -= 1
print(b)	