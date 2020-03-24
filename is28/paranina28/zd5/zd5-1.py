
def vvod():
	m=4
	n=4
	f = open('data.txt', 'r')
	a = []
	for i in range(m):
		a.append([])
		for j in range(n):
			a[i].append(int(f.readline()))
	return a

def rachet(a):
    i = int(input("i= "))
    k = int(input("k= "))
    u=a[i]
    a[i]=a[k]
    a[k]=u
    return a
    
def vyvod(result):
    f = open('result.txt', 'w')
    print(result, file = f)


    
a = vvod()  
result = rachet(a) 
vyvod(result)
    
    

