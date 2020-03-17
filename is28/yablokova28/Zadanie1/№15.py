a=1000
b=1
c=1
s=0
while b<= a:
  s+=b
  (b,c)=(c,b+c)
print(s)    
  