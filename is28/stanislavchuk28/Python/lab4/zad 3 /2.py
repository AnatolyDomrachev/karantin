print("Введите число:") 
x=int(input())
def vvod_dannyh(): 
    print("Ввод исходных данных") 
    a=[]
    for i in range(0,10): 
        a.append(int(input())) 
    return a
def add(a,x):
	print("a=",a," x=",x)
	if x in a:
		return True
	else:
		return False


#главный модуль 
dannye = vvod_dannyh() 
result = add(dannye,5)
print(result)

