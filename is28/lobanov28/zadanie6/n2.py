def slovar():
	
	data = open('data.txt', 'r')
	a = []
	b = {}
	
	for i in range(5):
		slvr = data.readline()
		y = slvr.split(" ")
		b["name"] = y[0]
		b["surname"] = y[1]
		a.append(b.copy())
	
	return a
def raschet(arr, strk):
	res = []
	for k in arr:
		if strk == k['name'] or strk == k['surname']:
			res.append(k)
	return res

res = slovar()
print(res)
strk = input("Введите строку ")
res1 = raschet(res, strk)
if res1:
	print(res1)
else:
	print(res)