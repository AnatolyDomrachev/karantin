def vvod():
    a = []
    for i in range(10):
        x = float(input())
        a.append(x)
    return a

def rachet(a):
    res = True
    for i in range(0,len(a)-1):
         if a[i]> a[i+1]:
              res = False
    return res

def vyvod(data):
    print(result)



data = vvod()
print(data)
result = rachet(data)
print(result)
vyvod(result)
print(vyvod)