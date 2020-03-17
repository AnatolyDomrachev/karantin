def str_search():
 d=str(input("введите строкy "))
 b=str(input("поиск: "))
 c=len(d)
 f=len(b)
 p=0
 n=0
 m=0
 for i in range(c):
   n=i
   if d[i]==b[0]:
     
     while d[i]==b[m]:
          p=p+1
          i=i+1
          
          if p>=f:
            break
          if m:
            break
 if p>=f:
  x=True
 else:
  x=False
 print(x)
 return()
str_search()
