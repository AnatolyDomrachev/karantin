import sys

a=input()
if a[len(a)-1]=='1':
 if a=='11':
  print (a+' лет')
  sys.exit()
 print (a+' год')
elif a[len(a)-1]=='2' or a[len(a)-1]=='3' or a[len(a)-1]=='4':
 if a=='12' or a=='13' or a=='14':
  print (a+' лет')
  sys.exit()
 print (a+' года')
else:
 print(a+' лет')
#if a[len(a-1)=='5' or a[len(a-1)=='6' or a[len(a-1)=='7' or a[len(a-1)=='8' or a[len(a-1)=='9' or a[len(a-1)=='0':
# print (a+' лет')