

a=input()
max=0
l=0
for i in range(len(a)):
	if a[i]!=' ':
		l=l+1
	else:
		if l>max:
			max=l
	if a[i]==' ':
		l=0
if l>max:
	max=l
print (max)
