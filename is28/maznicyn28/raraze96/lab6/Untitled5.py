def finder(a, b):
 bul = False
 for i in range(0, len(a) - len(b) + 1):
  c = 0
  if (a[i] == b[0]):
   if (len(b) > 1):
    for j in range(i + 1, i + len(b)):
     if (a[j] == b[c + 1]):
      c += 1
     else:
      c = 0
    if (c == len(b) - 1):
     bul = True
   else:
    bul = True
 return bul

a = input()
b = input()
n = finder(a, b)
print(n)