def func(text):
	f = open(text, 'r')
	mass = []
	for i in range(4):
		g = f.readline().replace('\n','')
		c = g.split(':')
		b = {"name": c[1], "number":c[0]}
		mass.append(b.copy())
	return(mass)
txt = input()
result = func(txt)
print(result)
