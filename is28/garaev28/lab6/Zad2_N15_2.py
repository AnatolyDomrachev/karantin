import random

#def chk_max(b,maxa,maxj):
# for k in range (len(b)):
#  if maxa<a[k][maxj]:
#   continue
#  else:
#   return (0)
#  return(1)



a=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for i in range(len(a)):
 for j in range(len(a[i])):
  a[i][j]=random.randint(0, 2)
  #a[i][j]=int(input())
  
print (a[0][0],' ',a[0][1],' ',a[0][2],' ',a[0][3],' ',a[0][4])
print (a[1][0],' ',a[1][1],' ',a[1][2],' ',a[1][3],' ',a[1][4])
print (a[2][0],' ',a[2][1],' ',a[2][2],' ',a[2][3],' ',a[2][4])
print (a[3][0],' ',a[3][1],' ',a[3][2],' ',a[3][3],' ',a[3][4])
print (a[4][0],' ',a[4][1],' ',a[4][2],' ',a[4][3],' ',a[4][4])
  
for i in range(len(a)):
 mina=1000
 maxa=0
 mini=0
 minj=0
 maxi=0
 maxj=0
 ok=0
 for j in range (len(a[i])):
  if a[i][j]>maxa:
   maxa=a[i][j]
   maxi=i
   maxj=j
  if a[i][j]>mina:
   mina=a[i][j]
   mini=i
   minj=j
# if chk_max(a,maxa,maxj)==1:
#  print(maxi,' ',maxj)
