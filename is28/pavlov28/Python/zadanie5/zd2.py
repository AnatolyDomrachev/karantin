def vvod():
	a = []
	f = open('data2.txt', 'r')
	for i in range(10):
		n = f.readline()
		a.append(n)
	return a	
	
def raschet_vyvod(a):
	result = 0
	for j in range(n-1):
		for g in range(j+1, n):
			if a[j] == a[g]:
				f = open('res2.txt', 'w')
				print("В резyльтате работы программы был полyчен следyющий резyльтат: ", True, file = f );
				quit()
	f = open('res2.txt', 'w')
	print("В резyльтате работы программы был полyчен следyющий резyльтат: ", False, file = f );
	
	

a = vvod()	
raschet_vyvod(a)





