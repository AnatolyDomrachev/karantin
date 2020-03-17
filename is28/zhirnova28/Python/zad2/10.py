import random
M=4
N=4
a=[]
for i in range(M):
 for i in range(N):
  x=int(input("Введите элементы матрицы:"))
  a.append(x)
print(a)
print("Минимальный элемент равен:", min(a))
print("Максимальный элемент равен:", max(a))
k=max(a)-min(a)
print(k)
