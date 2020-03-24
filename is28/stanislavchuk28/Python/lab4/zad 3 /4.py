def vvod_dannyh(): 
	
	a=[]
	for i in range(0,10): 
	a.append(float(input())
	
    return a
def raschet(data):
	print("Массив: ",data)    
def ras(a):
	for i in range(1,len(a)): 
		if a[i-1]<a[i]:
			return True
		else:
			return False
		

#главный модуль 
dannye = vvod_dannyh() 
raschet(dannye)
result=ras(dannye)
print(result)

