result=True
i = 0
a=[]
for i in range(10):
	x = float(input())
	a.append(x)

for i in a:	
	print(i)
	
for i in range(0,len(a)-1):
	if a[i]	> a[i+1]:
		result=False
print(result)


