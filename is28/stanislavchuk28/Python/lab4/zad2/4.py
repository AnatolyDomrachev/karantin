result=True
a=[]
for i in range (10):
	b=int(input());
	a.append(b)
print(a)

for i in range(1,len(a)):
	if a[i-1]<a[i]:
		result=False

print(result)
