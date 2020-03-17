a = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
b = [0,0,0,0]
for i in range(0,4):
 for j in range(0,4):
  a[i][j] = int(input())
for i in range(0,4):
 b[i] = int(input())

c = int(input())
for i in range(0,4):
 a[i][c - 1] = b[i]
for i in range(0,4):
 print(str(a[i][0]) + str(a[i][1]) + str(a[i][2]) + str(a[i][3]))

