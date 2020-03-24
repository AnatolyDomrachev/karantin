def func(text):
	f = open(text, 'r')
	mass = []
	for i in range(0,3):
		 g = f.readline().replace('\n','')
		 c = g.split(':')
		 b = {"name":c[1], "age":c[0]}
		 mass.append(b.copy())
	return(mass)
txt = input() #ввод имени файла
result = func(txt)
print(result)
