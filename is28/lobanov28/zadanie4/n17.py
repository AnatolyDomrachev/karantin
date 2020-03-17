def vvod_dannyh():
	x = str(input("Введите строкy "))
	a = str(input("Введите слово "))
	return x, a
def raschet(x, a):
	return x.split().count(a)

def vyvod_resultata(a):
	print(a)
x, a= vvod_dannyh()
res = raschet(x, a)
vyvod_resultata(res)