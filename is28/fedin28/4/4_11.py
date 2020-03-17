def func(a, b):
    c=[]
    a=a.strip()
    b=b.strip()
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j]:
                c.append(a[i])
    return c
    
    
    
str1=input()
str2=input()
c=func(str1, str2)
print(c)