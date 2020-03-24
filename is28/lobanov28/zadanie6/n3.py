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
def raschet(res):
	 
	s = {}
	s['name'] = input("Введите Имя ")
	s['surname'] = input("Введите Фамилию ")
	
	res.append(s.copy())
	
	return res

def vyvod_dannyh(qq):
	f = open('data2.txt', 'w')
	for x in qq:
		print(x['name']+" \t "+x['surname'], file=f)

res = slovar()
print (res)
qq = raschet(res)
print(qq)
vyvod_dannyh(qq)