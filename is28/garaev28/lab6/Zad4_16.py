def chkword (a,b):
    ok=-1
    if a[0:len(b)]!=b:
        for i in range(0,len(a)):
            if a[i]==' ':
                if a[i+1:i+1+len(b)]==b:
                    ok=1
                    break
    else:
        ok=1
    return ok

x=str(input())
y=str(input())
print(chkword(x,y))