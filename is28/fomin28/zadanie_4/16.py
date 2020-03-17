stroka=str(input('vvod stroki: '))
slovo=str(input('vvod slova: '))
a=[]
a=stroka.split(' ')
for i in range(len(a)):
   if a[i] == slovo:
     x=1
   else:
     x=0
     break
if x==1:
  ans=str('slovo est`')
else:
  ans=str('slova net')
print(ans)
