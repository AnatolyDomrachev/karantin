def counts(a):
 b = [];
 i = 0;
 k = 0;
 while i < len(a):
  if (a[i] != " "):
   k += 1;
   i += 1;
  else:
   b.append(k);
   k = 0;
   i += 1;
 b.append(k);
 return b
a = input()
c = counts(a)
print (c)