def vvod():
    f = open('data.txt', 'r')
    a = []
    
    for i in range(10):
        x = float(f.readline())
        a.append(x)
    return a

def rachet(a):
    res = True
    for i in range(0,len(a)-1):
         if a[i]> a[i+1]:
              res = False
    return res

def vyvod(data):
    f = open('result.txt', 'w')
    print(result, file = f)



data = vvod()
print(data)
result = rachet(data)
print(result)
vyvod(result)