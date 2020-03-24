k=int(input("Введите позицию числа = "))
a=[]
b=[]
for j in range(0,90):
	a.append(10+j)
for i in range(0,90):
	b.append(int(a[i]/10))
	b.append(int(a[i]%10))
print(b[k-1])