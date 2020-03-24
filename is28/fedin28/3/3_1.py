
def vvod():
    a = []
    for i in range(n):
        a.append(int(input())) 
    return a

def ras(a):
    b=0
    for i in range(n):
        b = b+a[i]
    return b


def dpo(b):
    c = b/n
    print(c)


n = int(input())
a=vvod()
b=ras(a)
dpo(b)