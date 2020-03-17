def strfind(a,b):
    o=int(-1)
    for i in range(0,len(a)-len(b)+1):
        #print(i,', ',a[i:i+len(b)])
        if a[i:i+len(b)]==b:
            o=int(i)
            break
    return o

x=str(input('Введите исходную строку: '))
y=str(input('Введите искомую строку: '))
#print(len(y),' ',len(x)-len(y))
print(strfind(x,y))