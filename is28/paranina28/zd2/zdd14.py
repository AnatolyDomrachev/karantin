a=[]
b=[]
m=4
n=4
for i in range(m):
  a.append([])
  for j in range(n):
     a[i].append(int(input()))
print(a)
for j in range(m):
  b.append([])
  for i in range(n):
     b[j].append(a[i][j])
print(b)



