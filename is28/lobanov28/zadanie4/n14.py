def vvod_dannyh():
	x = str(input("Введите строкy: "))
	return x
def raschet(x):
	a = (x.split())
	for i in range(len(a)):
		a[i] = len(a[i])
	return a 
def vyvod_resultata(a):
	print(a)
x = vvod_dannyh()
res = raschet(x)
vyvod_resultata(res)

	