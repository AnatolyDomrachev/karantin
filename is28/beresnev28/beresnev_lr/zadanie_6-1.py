def slov_in(a):
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

a=input('введите имя файла = ')
print(slov_in(a))
