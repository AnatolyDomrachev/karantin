def massivslovare():
    f=open('file6.txt','r')
    a=[]
    v={}
    for i in range(2):
        buf = f.readline()
        buf1 = buf.split(':')
        v['name']=buf1[0]
        v['surname']=buf1[1]
        v['age']=int(buf1[2])
        a.append(v.copy())
    return a

vyvod=massivslovare()
print(vyvod)
