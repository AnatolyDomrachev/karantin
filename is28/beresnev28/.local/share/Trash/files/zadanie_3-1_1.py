def input_ar():
	a=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	for w in range(4):
		for e in range(4):
			a[w][e]=int(input("Введите элемент массива = "))
	print(a[0])
	print(a[1])
	print(a[2])
	print(a[3])

	return(a)

def sort_ar(a):
	s=a[1][1]
	for k in range(4):
		for u in range(4):
			if  a[k][u] >= s:
				s=a[k][u]
				str=k
				sto=u
	return s,str,sto

a=input_ar()
s,str,sto=sort_ar(a)
print("наибольшее число = ", s,"строка = ",str+1,"столбец = ",sto+1) 