a = []         
n = int(input())  
for i in range(n):
   a.append(int(input())) 
e=a[0]
for i in range(1, n):
    if e<a[i]:
      e=a[i] 
y=a[0]
for i in range(1, n):
    if y>a[i]:
      y=a[i] 
print("Ответ: ", e-y)

  
  
  

 

  

 
  
