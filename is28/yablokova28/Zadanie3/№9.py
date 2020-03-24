import random

def vvod_massiva():
	b = []
	c = []
	d = []
	f = []
	a = [b, c, d, f]
	for i in range (4):
		x = random.randint(0,100)
		b.append(x)
	for i in range (4):
		x = random.randint(0,100)
		c.append(x)
	for i in range (4):
		x = random.randint(0,100)
		d.append(x)
	for i in range (4):
		x = random.randint(0,100)
		f.append(x)
	return (a)
	
def poisk_maximuma(massiv):
	maximum  = 0
	for i in range (4):
		for j in range (4):
			 if massiv[i][j] > maximum:
				maximum = massiv[i][j]
				x = i+1                 # N stroki
				y = j+1                 # N stolba
	return (maximum, x, y)

def m_elem_strk_stl (elem, strk, stl):
	print ("", elem)
	print ("", strk)
	print ("", stl)
	return ()


m = vvod_massiva()
print(m)
sbel = poisk_maximuma (m)
ivf = m_elem_strk_stl (sbel[0],sbel[1],sbel[2])