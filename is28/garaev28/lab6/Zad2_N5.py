a={}
b=0
for i in range (0,5):
 a[i]=int(input())
 
for i in range (0,4):
 for j in range (i+1,5):
  if a[i]==a[j]:
   b=1

if b==1:
 print('Имеются повторы')
else:
 print('Повторов нет')