a=[]
b=[]
m=4
n=4
for i in range(m):
  a.append([])
  for j in range(n):
     a[i].append(int(input()))
print(a)
for l in range(n):
  b.append(int(input()))
print(b)
j=int(input("введите j="))
for k in range(m):
   a[k][j]=b[k]
print(a)
   