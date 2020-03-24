k = int(input())
a = []
for i in range(30):
	if i<10:
		a.append(i)
	else :
		a.append(i//10)
		a.append(i%10)
print(a)	
print(a[k]) 