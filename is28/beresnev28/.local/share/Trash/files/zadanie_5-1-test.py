def input_ar():
	f=open('zadanie_5-1_input.txt', 'r')
	a=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	for w in range(4):
		for e in range(4):
			ch=int(f.readline())
			a[w][e]=ch

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
f=open('zadanie_5-1_output.txt','w')
print("наибольшее число = ", s,", строка = ",str+1,", столбец = ",sto+1, file = f) 