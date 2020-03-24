def slovar():
	
	h_file = open('slovar.txt', 'r')
	a = []
	b = {}
	
	for i in range(4):
		c = h_file.readline()
		d = c.split(":")
		b["first"] = int(d[0])
		b["second"] = int(d[1])
		a.append(b.copy())
	
	return a

res = slovar()
print (res)