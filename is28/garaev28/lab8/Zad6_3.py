def input_arr(x):
	a=[]
	f=open(x,"r")
	y=f.readline()
	while y!="":
		z=y.split(":")
		b={"name":z[0],"id":int(z[1])}
		a.append(b)
		y=f.readline()
	f.close()
	return a
	
def output_arr(b):
	f=open('output.txt','w')
	for i in range (0,len(b)):
		f.write(str(b[i])+'\n')
	
def add_sl(a,x):
	f=open(x,'r')
	y=f.readline()
	while y!='':
		z=y.split(":")
		b={"name":z[0],"id":int(z[1])}
		a.append(b)
		y=f.readline()
	f.close()
	return a
			
a=input('Введи исходный файл: ')
b=[]
b=input_arr(a)
c=input('Введите файл, который необходимо добавить: ')
d=add_sl(b,c)
output_arr(d)

 