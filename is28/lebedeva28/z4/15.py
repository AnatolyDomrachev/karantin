print("Введите строкy: ")
string=input()
a=string.split()
b=[]
for i in range(len(a)): 
	b.append(len(a[i]))
for i in range(len(b)):
	j=b[0]
	if j>b[i]:
		j=b[i]
print(j)
