def func(text):
	f = open(text, 'r')
	mass=[]
	
	for i in range(3):
		g=f.readline().replace('\n','')
		c=g.split(':')
		b={"name": c[1], "age":c[0]}
		mass.append(b.copy())
		
	c=input('name')
	C=int(input('age'))
	b={"name": c, "age": C}
	mass.append(b.copy())
	F=open('res3.txt', 'w')
	print(mass, file=F)
	return mass
	
txt=input()
result=func(txt)




