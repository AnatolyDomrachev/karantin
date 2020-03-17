def vvod_dannyh():
 a = [];
 for i in range(0,10):
  a.append(int(input()));
 return a;
def raschet(a):
 for i in range(1,10):
   k = i - 1;
   j = i;
   while (a[k] < a[j]):
    if (a[k] < a[j]):
     a[k],a[j] = a[j],a[k];
     if (k > 0):
      k -= 1;
      j -= 1;
 return a
def vyvod_resultata():
 print(a);
a = vvod_dannyh();
a = raschet(a);
vyvod_resultata(); 