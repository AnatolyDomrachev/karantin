a=[]
m=4
n=4
for i in range(m):
  a.append([])
  for j in range(n):
     a[i].append(int(input()))
print(a)
y=a[0][0]
z=0
for k in range(m):
  if y<a[k][0]:
    y=a[k][0]
    z=k
u=a[0]
a[0]=a[z]
a[z]=u
print(a)