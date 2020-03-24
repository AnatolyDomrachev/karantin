
def vvod(): 
	res=[]
	for i in range(5):
		n=float(input())
		res.append(n)
	return res
	
def raschet(x,y,z):

	res = 0
	if min(x)>min(y) and min(x)>min(z):res = x
	if min(y)>min(x) and min(y)>min(z):res = y
	if min(z)>min(x) and min(z)>min(y):res = z
	return res
   
def vyvod(res):
	print('массив, ó которого самый большой минимальный элемен')
	print(res)

print('1 массив')	
x=vvod()
print("2 массив")
y=vvod()
print('3 массив')
z=vvod()

res = raschet(x,y,z)
vyvod(res)
'''
print('самый большой минимальный элемен')
if min(x)>min(y) and min(x)>min(z):print(x)
if min(y)>min(x) and min(y)>min(z):print(y)
'''











