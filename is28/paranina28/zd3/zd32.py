m=4
n=4

def vvod1():
    a = []
    for i in range(m):
      a.append([])
      for j in range(n):
        a[i].append(int(input()))
    return a
    
def vvod2():
    b = []
    for l in range(n):
      b.append(int(input()))
    return b
    
def rachet(a,b):
    j=int(input("введите j="))
    for k in range(m):
      a[k][j]=b[k]
    return a
    
def vyvod(result):
    print(result)


a = vvod1()  
b = vvod2()  
result = rachet(a,b) 
vyvod(result)
