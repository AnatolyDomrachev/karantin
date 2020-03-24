def nodif(s1,s2):
    a=[]
    s1=list(s1)
    s2=list(s2)
    for c in range(len(s1)):
        for g in range(len(s2)):
            if s1[c] == s2[g]:
                a.append(s1[c])
    return(a)
s1=str(input("строка1 = "))
s2=str(input("строка2 = "))
f=nodif(s1,s2)
print(f)
