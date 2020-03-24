def func(a, b):
 c=[]
 for i in range (len(a)):
  for j in range (len(b)):
   if a[i]==b[j]:
    c.append(a[i])
 return c
 


str1=input("Введите 1 строкó:")
str2=input("Введите 2 строкó:")
c=func(str1, str2)
a=set(c)
print("Вывод значений, которые имеются в обоих строках")
print()
print (a)