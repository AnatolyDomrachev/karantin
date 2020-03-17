def slow(name):
	m=[]
	f = open(name, 'r')
	st=f.readline().replace('\n','')
	while st != "" :
		st_m=st.split(":")
		s={'name': st_m[0],'age':st_m[1]}
		m.append(s)
		st=f.readline().replace('\n','')
	a=input("Введите name: ")
	b=input("Введите age: ")
	sl={'name': a,'age':b}
	m.append(sl)
	f = open(name, 'w')
	print(m, file = f)
	return m
name=input("Введите название файла =")
m=slow(name)
