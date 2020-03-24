x=[]
print("Введите данные массива")
n=0
for i in range(10):
 y=int(input())
 x.append(y)
for i in range(0,len(x)-1):
 if ((x[i-1]<x[i] and x[i+1]<x[i] or x[i-1]>x[i] and x[i+1]>x[i])):
  n+=1
print("Количество поворотных точек:",n)  