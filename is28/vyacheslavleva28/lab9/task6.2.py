
def slovar():
	
	h_file = open('slovar.txt', 'r')
	a = []
	b = {}
	
	for i in range(4):
		c = h_file.readline()
		d = c.split(":")
		b["first"] = d[0]
		b["second"] = d[1]
		a.append(b.copy())
	
	return a
	
def func_2(arr, stroka):
	res = []
	for el in arr:
		if stroka == el['first'] or stroka == el['second']:
			res.append(el)
	return res

res = slovar()
print (res)
stroka = input("Введите строкy")
res2 = func_2(res, stroka)
if res2:
	print (res2)
else:
	print (res)



