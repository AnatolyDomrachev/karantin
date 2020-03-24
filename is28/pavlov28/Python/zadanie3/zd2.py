def vvod_n():
	print("Количество чисел в списке: ")       
	n = int(input())
	return n

def vvod(n):
	print("Ввод списка ")
	a = []
	for i in range(n):
		a.append(int(input())) 
	return a	
	
def raschet_vyvod(a):
	result = 0
	for j in range(n-1):
		for g in range(j+1, n):
			if a[j] == a[g]:
				result = True
				return result
				quit()
	result = False
	return result
	
	
n = vvod_n()
a = vvod(n)	
res = raschet_vyvod(a)
print(res)

