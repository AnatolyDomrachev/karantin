import random 
def vvod():
	b = []
	c = []
	d = []
	f = []
	arr = [b, c, d, f]

	for i in range(4):
		x = random.randint(0, 100)
		b.append(x)
		
	for i in range(4):
		x = random.randint(0, 100)
		c.append(x)
		
	for i in range(4):
		x = random.randint(0, 100)
		d.append(x)
		
	for i in range(4):
		x = random.randint(0, 100)
		f.append(x)
		
	print(arr)
	return(arr)

def raschet(arr):
	max = 0
	for i in range(4):
		for j in range(4):
			if arr[i][j]>max:
				max=arr[i][j]
	#print(max)
	return(max)

def vyvod(max):
	print(max)



arr = vvod()
max = raschet(arr)
vyvod(max)
