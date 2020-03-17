a=int(input("Конечное число:"))
b=c=1
print(0)
while b <= a:
	print(b)
	(b, c) = (c, b + c)
	
	
	
a=b=1
n=int(input("Номер числа Фибоначчи:")) - 3
while n>0:
	a, b = b, a+b
	n -= 1
print(b)	