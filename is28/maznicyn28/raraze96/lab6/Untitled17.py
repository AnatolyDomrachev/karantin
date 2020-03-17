def finder_wrd(a, b):
 f = 0;
 
 for i in range(0, len(a) - len(b) + 1):
  bul = False;
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
  if (bul):
    f += 1;
    
 return f

a = input()
b = input()
s = finder_wrd(a, b)
print (s)