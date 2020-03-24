a = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
b = [[0,0,0], [0,0,0], [0,0,0]]
k = 0
f = 0
for i in range(0,4):
 for j in range(0,4):
  a[i][j] = int(input())
w = int(input())
v = int(input())
for i in range(0,4):
 if i == w:
  continue
 else:
  for j in range(0,4):
   if j == v:
    continue
   else:
    b[k][f] = a[i][j]
    f = f + 1
  k = k + 1
  f = 0
for i in range(0,3):
 print(str(b[i][0]) + str(b[i][1]) + str(b[i][2]))