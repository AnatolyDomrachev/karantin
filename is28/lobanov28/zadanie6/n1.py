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
res = slovar()
print (res)