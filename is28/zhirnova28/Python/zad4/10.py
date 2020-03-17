def vvod():
 global s1
 s1=str(input())
 return s1
 
def res():
 for x in reversed(s1):
  print(x)
 return x
 
s1=vvod()
y=res()
