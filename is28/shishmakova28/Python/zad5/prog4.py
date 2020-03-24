def func(a):
    c=0
    for i in range(9):
        if a[i]<a[i+1]:c=c+1
    if c==9: res = 'Yes'
    else: res = 'No'
    return res
    
def vvod():
    f=open('file2.txt','r')
    a=[]
    c=0
    for i in range(10):
        b=float(f.readline())
        a.append(b)
    return a

arr=vvod()
c = func(arr)

f=open('File2(end).txt','w')
print(c,file=f)
