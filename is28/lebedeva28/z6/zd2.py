def voc():
	f=open('data.txt', 'r')
	a=[]
	b={}
	for i in range(3):
		c=f.readline().replace('\n', '')
		d=c.split(":")
		b['Name']=d[0]
		b['Age']=d[1]
		a.append(b.copy())
	return a
	
	
def func(mass, string):
	res=[]
	for i in mass:
		if string == i['Name'] or string == i['Age']:
			res.append(i)
	return res
	
	
res=voc()
print(res)
string=input('Введите строкy: ')
res2=func(res, string)
if res2:
	print(res2)
else:
	print(res)
			




