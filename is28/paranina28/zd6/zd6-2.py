def slow(name):
	m=[]
	f = open(name, 'r')
	st=f.readline().replace('\n','')
	while st != "" :
		st_m=st.split(":")
		s={'name': st_m[0],'age':st_m[1]}
		m.append(s)
		st=f.readline().replace('\n','')
	return m
	
def poisk(m, st):
	if st == '':
		print("name \t age")
		for x in m:
			print(x['name']+" \t "+x['age'])
	else:
		for i in m:
			if i['name'] == st:
				print(i)
			if i['age'] == st:
				print(i)
	return m
name=input("Введите название файла =")
st=input("Введите cтрокy:")
m=slow(name)
poisk(m, st)