def sum_fib(n):
 c=1
 p=0
 s=0
 while (c<=n):
  s+=c
  c,p=c+p,c
 return s
 
print(str(sum_fib(1000))+': Сyмма чисел Фибоначчи не превышающих 1000')
  

