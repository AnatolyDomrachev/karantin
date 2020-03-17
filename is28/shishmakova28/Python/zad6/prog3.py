def massivslovare():
    f=open('file6.txt','r')
    a=[]
    v={}
    for i in range(2):
        buf = f.readline()
        buf1 = buf.split(':')
        v['name']=buf1[0]
        v['surname']=buf1[1]
        v['age']=int(buf1[2])
        a.append(v.copy())
    f.close()
    return a


def nov_slovara():
	v={}
	v['name']=str(input('имя: '))
	v['surname']=str(input('фамилия: '))
	v['age']=int(input('возраст: '))
	return v
	
def dobavlenie_slovare(mas,sl):
	mas.append(sl)
	return mas


def vyvod(res):
	f=open('file6.txt','w')
	for x in res:
		print(x['name']+':'+x['surname']+':'+str(x['age']), file=f)

	

massiv=massivslovare()
slovare=nov_slovara()
nov_massiv=dobavlenie_slovare(massiv,slovare)
konec=vyvod(nov_massiv)
