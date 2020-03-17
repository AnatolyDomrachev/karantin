m=4
n=4

def vvod():
    a = []
    for i in range(m):
      a.append([])
      for j in range(n):
        a[i].append(int(input()))
    return a

def rachet(a):
    i = int(input("i= "))
    k = int(input("k= "))
    u=a[i]
    a[i]=a[k]
    a[k]=u
    return a
    
def vyvod(result):
    print(result)


    
a = vvod()  
result = rachet(a) 
vyvod(result)
    
    

