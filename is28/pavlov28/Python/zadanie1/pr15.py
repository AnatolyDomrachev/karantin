a=1000
b=1
c=1
sum = 0
while b <= a:
  sum=sum+b
  (b, c)=(c, b + c)
print(sum)  
