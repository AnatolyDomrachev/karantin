import random
a=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
b=[0,0,0,0]
for i in range(len(a)):
 for j in range(len(a[i])):
  a[i][j]=random.randint(1, 100)

print('Введите вектор')
for i in range(len(b)):
 b[i]=int(input())

z=int(0)
r=0
while r!=1:
 print('Какой столбец необходимо заменить?')
 z=int(input())
 if z==1 or z==2 or z==3 or z==4:
  r=1
 
z=z-1
for i in range(len(a[i])):
 a[i][z]=b[i]

print (a[0][0],' ',a[0][1],' ',a[0][2],' ',a[0][3])
print (a[1][0],' ',a[1][1],' ',a[1][2],' ',a[1][3])
print (a[2][0],' ',a[2][1],' ',a[2][2],' ',a[2][3])
print (a[3][0],' ',a[3][1],' ',a[3][2],' ',a[3][3])

 