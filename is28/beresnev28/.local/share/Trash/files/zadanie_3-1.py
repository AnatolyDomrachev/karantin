x=[]
def input_d():
	for i in range(5):
		x.append(int(input('Введите элемент массива = ')))
	return(x)

def sort_a(x):
	for j in range(4):
		for k in range(4):
			if x[k] < x[k+1]:
				x[k],x[k+1]=x[k+1],x[k]
	return(x)
x=input_d()
print(x)
x=sort_a(x)
print(x)
	