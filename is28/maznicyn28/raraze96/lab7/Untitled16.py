def vvod():
 a = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
 f = open("data.txt", "r");
 for i in range(0,4):
  for j in range(0,4):
   n = int(f.readline())
   a[i][j] = n;
 n = int(f.readline())
 stroc = n;
 n = int(f.readline())
 stol = n;
 f.close();
 return a, stroc, stol;
def telo(a, stroc, stol):
 b = [[0,0,0], [0,0,0], [0,0,0]]
 k = 0;
 f = 0;
 for i in range(0,4):
  if i == stroc:
   continue
  else:
   for j in range(0,4):
    if j == stol:
     continue
    else:
     b[k][f] = a[i][j]
     f = f + 1
   k = k + 1
   f = 0
 return b;
def vyvod():
 f = open("res.txt", "w");
 for i in range(0,3):
  f.write(str(b[i][0]) + str(b[i][1]) + str(b[i][2]) + "\n")
 f.close();
a, stroc, stol = vvod();
b = telo(a,stroc,stol);
vyvod();
 

 
   