a=[]
c=0
for i in range(5):
	b=float(input())
	a.append(b)
for i in range(4):
	if a[i]<a[i+1]:c=c+1
if c==4: print('Yes')
else: print('No')