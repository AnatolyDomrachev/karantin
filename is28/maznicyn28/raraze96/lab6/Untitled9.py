def deko(a, m, n):
 b =[]
 for i in range(0, len(a)):
  if (i >= n - 1) and (i < m + n - 1):
   continue;
  b.append(int(a[i]))
 return b
a = input();
m = int(input());
n = int(input());
z = deko(a, m, n);
k = ""
for i in range(0, len(a) - m):
 k += str(z[i])
print(k)