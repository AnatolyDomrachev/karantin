def func(text):
	f = open(text, 'r')
	mass = []
	str = f.readline()
	for i in range(1,5):
		g = f.readline().replace('\n','')
		c = g.split(':')
		if str in c:
			b = {"name": c[1], "number":c[0]}
			print(b)		
		b = {"name": c[1], "number":c[0]}
		mass.append(b.copy())
		if str == '':
			print(mass)
	return(mass)
	
txt = input()
func(txt)
#print(result)
