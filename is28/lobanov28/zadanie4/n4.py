def vvod_dannyh():
	x = float(input("Введите номер года"))
	return x	
def raschet(x):
	if ((x % 4 == 0) and (x % 100 > 0)) or x % 400 == 0:
		x = 1
	else: x = 0
	return x
def vyvod_resultata(x):
	print(x)
x = vvod_dannyh()
res = raschet(x)
vyvod_resultata(res)