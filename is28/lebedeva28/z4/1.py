
def func(n):
	print("Ввод списка ")
	v=[]
	for i in range(n):
		v.append(int(input()))
	print("Введите число X: ")
	x = int(input())
	k=0
	m=0
	for i in range(n):
		if v[i] == x:
			print(i)
			quit()		
	print(False)
	
print("Количество чисел в списке: ")
n=int(input())
func(n)

				