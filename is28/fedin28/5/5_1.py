
def vvod():
    a = []
    f = open('data.txt','r')
    for i in range(10):
        n = int(f.readline())
        a.append(n)
    return a

def ras(a):
    b=0
    for i in range(10):
        b = b+a[i]
    return b


def dpo(b):
    c = b/10
    f = open('dpo.txt','w')
    print(c, file = f)


a=vvod()
b=ras(a)
dpo(b)