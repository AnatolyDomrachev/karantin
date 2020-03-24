def vvod_dannyh():
    print("Введите строку и два числа m и n, где m - количество символов, которые необходимо удалить, начиная с n-ого символа:")
    vvod=[]
    for i in range(3):
        vvod.append(input())
    return vvod

def process():
    c = 0
    m = int(dannye[1])
    n = int(dannye[2])-1
    stroka = list(dannye[0])
    length = len(stroka)
    result = []
    for i in range(m):
        if n+c<length:
            stroka.pop(n)
            c+=1
        else:
            c+=1
    return stroka
def vyvod_resultata():
    print(otvet)
################################################################################

dannye = vvod_dannyh()
otvet = "".join(process())
vyvod_resultata()
