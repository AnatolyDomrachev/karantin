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
    return a
	
def strochka():
	a=str(input('Введите строкó: '))
	return a
	
def proverka(a,b):
    if a == '':
        return b
    r=[]
    for i in b:
        if a==i['name']:
            r.append(i)
        if a==i['surname']:
            r.append(i)
        if a==i['age']:
            r.append(i)
    return r
	
mas1=massivslovare()
str1=strochka()
vyvod=proverka(str1,mas1)
print(vyvod)
