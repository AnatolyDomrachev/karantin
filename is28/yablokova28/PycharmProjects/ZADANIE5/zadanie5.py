def vvod_massiva():
    a = []
    with open('data.txt') as f:
        a = f.read().splitlines()
        b = []
        for i in range (len(a)):
            b.append(list(map(int, a[i].split())))
    return (b)

def poisk_maximuma(massiv):
    maximum = 0
    for i in range(4):
        if massiv[i][0] > maximum:
            maximum = massiv[i][0]
            index = i
    massiv[0], massiv[index] = massiv[index], massiv[0]
    return (massiv)

def vyvod_massiva(massiv):
    f = open ('result.txt', 'w')
    print(massiv, file=f)
    f.close()
    return ()

m = vvod_massiva()
for i in range (4):
    print(m[i])
sw_mstrk = poisk_maximuma(m)
print()
vyvod_massiva(sw_mstrk)

