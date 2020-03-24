def func(a):
    c=0
    for i in range(9):
            if a[i]<a[i+1]:c=c+1
    if c==9: res = 'Yes'
    else: res = 'No'
    return res

a=[]
c=0
for i in range(10):
	b=float(input())
	a.append(b)

c = func(a)
print(c)

