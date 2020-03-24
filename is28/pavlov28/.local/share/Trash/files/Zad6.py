import pickle
def asd(text):
	f = open(text, 'r')
	mass = []
	for i in range(0,3):
		 g = f.readline().replace('\n','')
		 c = g.split(':')
		 b = {"name":c[0], "cho_to":c[1]}
		 mass.append(b.copy())
	return(mass)
txt = input() #ввод имени файла
result = asd(txt)
print(result)
