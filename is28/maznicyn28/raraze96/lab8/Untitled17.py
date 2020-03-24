def vv():
 a = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]];
 b = [0,0,0,0];
 f = open("data2.txt", "r");
 for i in range(0,4):
  for j in range(0,4):
   n = int(f.readline());
   a[i][j] = n;
 for i in range(0,4):
  n = int(f.readline());
  b[i] = n;
 n = int(f.readline());
 ind = n;
 f.close();
 return a, b, ind;
def tel(a, b, ind):
 for i in range(0,4):
  a[i][ind - 1] = b[i]
 return a;
def vy():
 f = open("res2.txt", "w");
 for i in range(0,4):
  f.write(str(a[i][0]) + str(a[i][1]) + str(a[i][2]) + str(a[i][3]) + "\n")
 f.close();
a, b, ind = vv();
a = tel(a, b, ind);
vy();