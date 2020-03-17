a=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
b=[[],[],[],]
print(a[0])
print(a[1])
print(a[2])
print(a[3])
i=(int(input('введитe номер строки = '))-1)
k=(int(input('введите номер столбца = '))-1)

for f in range(4):
	a[f][k]=0

for t in range(4):
	a[i][t]=0
	
print(a[0])
print(a[1])
print(a[2])
print(a[3])


