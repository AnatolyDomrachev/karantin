def slov_in():
	a=input('введите имя файла с исходным словорём = ')
	arr=[]
	sl_ar={}
	f=open(a, 'r')
	sl=f.readline().replace('\n','')
	while sl != '' :
		sl_ar=sl.split(':')
		sl_ar_sl={'name':sl_ar[0],'age':sl_ar[1]}
		arr.append(sl_ar_sl)
		sl=f.readline().replace('\n','')
	return arr

def add_slov(arr):
	b1=input('name = ')
	b2=input('age = ')
	tmp={'name':b1,'age':b2}
	arr.append(tmp)
	a=input('введите имя файла для сохранения массива = ')
	f=open(a,'w')
	for o in arr:
		print(o['name'],':',o['age'],file = f)
	return
	
arr=slov_in()
add_slov(arr)



