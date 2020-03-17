def vvod():
	print("Ввод матрицы ")
	a = []
	for i in range (10):
		a.append(float(input()))
	return a	
	
def raschet(a):
	st = 0
	for i in range (9):
		if a[i] > a[i+1]:
			st = 1
	return st
	
def vyvod(st):
	if st == 0:
		ts = True
	else:
		ts = False
	return ts	
	
		
a = vvod()
st = raschet(a)
ts = vyvod(st)
print(ts)
		
		
			