#фóнкция чтения файла
def jojo():
	f = open('Jojo.txt', 'r')
	a = []
	b = {}
	for i in range(4):
		c = f.readline().replace('\n', '')
		d = c.split(":")
		b['Name'] = d[0]
		b['Number'] = d[1]
		a.append(b.copy())
	return a
	
def func(mass, str):
	res = []
	for i in mass:
		if str == i['Name'] or str == i['Number']:
			res.append(i)
	return res
	
res = jojo()
print(res)
str = input() #ввод строки
res2 = func(res, str)
if res2:
	print(res2)
else:
	print(res) 