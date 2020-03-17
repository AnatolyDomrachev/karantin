n = int(input("n= "))-3
if n<1:
 n = int(input("n= "))-3
a=b=1
while n>0:
  a,b=b,a+b
  n -= 1
print(b)  
 

