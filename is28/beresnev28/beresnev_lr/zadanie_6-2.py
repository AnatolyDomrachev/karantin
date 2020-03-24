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

def sl_search(arr,b):
	if b == '':
		print(arr)
	else:
		for k in arr:
			if k['name'] == b:
				print(k)
			if k['age'] == b:
				print(k)
	
	return 
a=input('введите имя файла со словорём = ')
b=str(input('введите строкy ='))
sl_search(slov_in(a),b)
