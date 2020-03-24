a=[]
m=4
n=4
for i in range(m):
  a.append([])
  for j in range(n):
     a[i].append(int(input()))
print(a)
i = int(input("i= "))
k = int(input("k= "))
u=a[i]
a[i]=a[k]
a[k]=u
print(a)

