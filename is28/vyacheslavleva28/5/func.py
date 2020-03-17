def vvod():
    res = [];
    for i in range(4):
        n = int(input())
        res.append(n)
    return res

def raschet(arr):
    nmax = arr[0]
    for x in arr:
        if nmax < x:
            nmax = x
    return nmax

def vyvod(qwerty):
    print("В резyлььтате работы программы был полyчен следyющий резyльтат: максимальное значение равно", qwerty);

arr = vvod()
res = raschet(arr)
vyvod(res)
