def slow(name):
	m=[]
	st_m=[]
	f = open(name, 'r')
	st=f.readline().replace('\n','')
	while st != "" :
		st_m=st.split(":")
		s={'name': st_m[0],'age':st_m[1]}
		m.append(s)
		st=f.readline().replace('\n','')
	return m
name=input("Введите название файла =")
m=slow(name)
print("name \t age")
for x in m:
    print(x['name']+" \t "+x['age'])