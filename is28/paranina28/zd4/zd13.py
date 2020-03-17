def sort_str(a):
	a=a+' '
	b=0
	k=0
	for y in a:
		if y != ' ':
			k+=1
		else:
			if k > b:
				b=k
			k=0
	return(b)
	
a=str(input('введи строкy ='))
b=sort_str(a)
print(b)
	