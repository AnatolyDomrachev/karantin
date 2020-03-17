def reverse(a):
    b=str('')
    i=len(a)-1
    while i!=-1:
        b=b+a[i]
        i=i-1
    return b

x=str(input())
print(reverse(x))