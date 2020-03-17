def vvod_str():
	a=str(input('Введите строкó:'))
	return a
	
	
def kolichestvo_simvolov(str1):
    a=len(str1)
    return a
    
def str_massiv(str1):
	x=[]
	a=kolichestvo_simvolov(str1)
	for i in range(a):
		x.append(str1[i])
	return x

def lishnie_probel(b):
	a=len(b)
	for i in range(a-1):
		if b[i]==b[i+1]==' ':
			b[i]=''
	return b

def massiv_str(b):
	for x in b:print(x, end='')
	print()
    
str1=vvod_str()   
b=str_massiv(str1)  
a=kolichestvo_simvolov(str1)
itog=lishnie_probel(b)
itog1=massiv_str(b)
