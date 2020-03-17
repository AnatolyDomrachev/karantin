def func(v):
	print("Введите число X: ")
	x = int(input())
	k=0
	for i in range(n):
		if v[i] == x:
			k=k+1
	return k
	
print("Количество чисел в списке: ")
n=int(input())
print("Ввод списка ")
v=[]
for i in range(n):
	v.append(int(input()))
b=func(v)
print(b)
		