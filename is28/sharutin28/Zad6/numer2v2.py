def tomato():
	file = open('Jojo.txt', 'r')
	a = []
	b = {}
	for i in range(4):
		c = file.readline()
		d = c.splite(":")
		b["first"] = d[1]
		a.append(b.copy())
		
	return a

def pomidorka(arr, str):
	res = [] 
	for i in arr:
		if str == i['first'] or stroka == i['second']:
		res.append(i)
	
	return res

res = tomato()
print(res)
str = input()
res2 = pomidorka(res, str)
if res2:
	print(res2)
else:
	print(res)
	