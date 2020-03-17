def func():
	v=[]
	f=open('data.txt', 'r')
	for i in range(10):
		n=int(f.readline())
		v.append(n)
	print('Введите число X: ')
	x=int(input())
	k=m=0
	print(v)
	for i in range(10):
		if v[i]==x:
			f=open('res.txt', 'w')
			print('В резyльтате работы программы был полyчен следyющий резyльтат: ', i, file=f)
			quit()
	f=open('res.txt', 'w')
	print('В резyльтате работы программы был полyчен следyющий резyльтат: ', False, file=f)

func()	