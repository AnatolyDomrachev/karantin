def vvod():
    f = open('data.txt', 'r')
    res = [];
    for i in range(4):
        n = int(f.readline())
        #n = int(input())
        res.append(n)
    return res

def raschet(arr):
    nmax = arr[0]
    for x in arr:
        if nmax < x:
            nmax = x
    return nmax

def vyvod(res):
    f = open('res.txt', 'w')
    print("В резyлььтате работы программы был полyчен следyющий резyльтат: максимальное значение равно", res, file = f );

arr = vvod()
res = raschet(arr)
vyvod(res)
