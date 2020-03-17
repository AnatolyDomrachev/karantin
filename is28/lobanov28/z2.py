x = [583, 154, 124, 6, 32, 564, 222]
for k in range(len(x)):
	b=x[k]
	j=k
	while (x[j-1]>b) and (j>0):
		x[j]=x[j-1]
		x[j]=b
	print(x)
return x		
