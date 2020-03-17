
def vvod():
    a = []
    for i in range(4):
        a.append([])
        for j in range(4):
            a[j].append(int(input()))
    return a


def ras(a):
    b=[]
    j=int(input())
    k=int(input())
    b=a[j]
    a[j]=a[k]
    a[k]=b
    return a           


def dpo(a):
    print(a)
    
    
a=vvod()
b=ras(a)
dpo(b)
