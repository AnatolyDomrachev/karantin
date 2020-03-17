print("Введите число:") 
x=int(input())
def vvod_dannyh(): 
    n = open('test.txt','r')
    a=[]
    for i in range(0,10): 
	 #n = int(input())
        a.append(n) 
    n.close();
    return a
def add(a,x):
	if x in a:
		return True
	else:
		return False

f=open('res.txt','w')		
f.close()

#главный модуль 
dannye = vvod_dannyh() 
result = add(dannye,x)
print(result)


