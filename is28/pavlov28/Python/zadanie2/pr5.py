a = []         
n = int(input())  
for i in range(n):
   a.append(int(input())) 
for j in range(n-1):
  for g in range(j+1, n):
    if a[j] == a[g]:
      print("Есть одинаковые")
      quit()
print("Нет одинаковых")
 

  

 
  
