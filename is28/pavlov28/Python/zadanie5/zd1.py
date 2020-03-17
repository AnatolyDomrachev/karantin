def vvod():
	v = []
	f = open('data1.txt', 'r')
	for i in range(10):
		n = f.readline()
		v.append(int(n))
	return v
	
def raschet(a):
	st = 0
	for i in range (9):
		if a[i] > a[i+1]:
			st = 1
	return st
	
def vyvod(st):
	if st == 1:
		f = open('res1.txt', 'w')
		print("В резyльтате работы программы был полyчен следyющий резyльтат: ", True, file = f );
	else:
		f = open('res1.txt', 'w')
		print("В резyльтате работы программы был полyчен следyющий резyльтат: ", False, file = f );

	
		
a = vvod()
st = raschet(a)
vyvod(st)

		
		
					
			
