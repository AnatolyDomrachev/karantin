import random

def vvod_massiva ():
	a=[]
	for i in range (4):
		b=[]
		for j in range (4):
			x = random.randint(0,100)
			b.append(x)
		a.append(b.copy())
	return(a)

def poisk_maximuma (massiv):
	maximum = 0
	for i in range (4):
		if massiv[i][0] > maximum:
			maximum = massiv[i][0]
			index = i
	massiv[0], massiv[index] = massiv[index], massiv[0]
	return(massiv)

def vyvod_massiva(massiv):
	for i in range (4):
		print(massiv[i])
	return()
	
m = vvod_massiva()
for i in range (4):
	print(m[i])
sw_mstrk = poisk_maximuma(m)
print()
vyvod_massiva(sw_mstrk)
	