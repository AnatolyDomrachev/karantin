def delete(a,b,c):
    d=a[0:b-1]+a[b+c-1:len(a)]
    return d

x=str(input())
m=int(input())
n=int(input())
print(delete(x,m,n))