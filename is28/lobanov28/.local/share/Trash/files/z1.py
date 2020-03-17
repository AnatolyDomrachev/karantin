x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
z = [3, 6, 9, 12, 15]
m=x[0]
m1=y[0]
m2=z[0]
for i in range(4):
	if x[i]>m:
		m=x[i];
for k in range(4):
	if y[k]>m1:
		m1=y[k]
for j in range(4):
	if z[j]>m2:
		m2=z[j]
a[m, m1, m2]
print(a)
