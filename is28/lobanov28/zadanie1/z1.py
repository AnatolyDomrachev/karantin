x = [123, 33, 56, 65, 23]
y = [67, 36, 66, 35, 132]
z = [23, 16, 23, 12, 151]
m=x[0]
m1=y[0]
m2=z[0]
for i in range(5):
	if x[i]<m:
		m=x[i];
for k in range(5):
	if y[k]<m1:
		m1=y[k]
for j in range(5):
	if z[j]<m2:
		m2=z[j]
print(m)
print(m1)
print(m2)
mx=m
if m>m1 and m>m2:
	mx=m
if m1>m and m1>m2:
	mx=m1
if m2>m1 and m2>m:
	mx=m2
print(mx)
