def array_inp(a):
	b=[]
	f=open(a,'r')
	x=f.readline()
	while x!="":
		c=x.split(":")
		z={'1':c[0],'2':int(c[1])}
		b.append(z)
		x=f.readline()
	f.close
	return b
	
def search(a,s):
	for i in range(len(a)):
		if (str(b[i]['1']) == s)or(str(b[i]['2']) == s):
			print (b[i])
		
a=input('Введите имя файла: ')
s=input('Введите строкó: ')
b=[]
b=array_inp(a)
search(b,s)