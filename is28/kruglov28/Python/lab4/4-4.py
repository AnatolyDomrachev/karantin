def vvod_dannyh():
    print("Функция вернёт 1, если год високосный и 0, если год невисокосный.")
    print("Введите номер года:")
    vvod=int(input())
    return vvod

def raschet():
    if nomer_goda%4==0 and (nomer_goda%100!=0 or nomer_goda%400==0):
        god = 1
    else:
        god = 0
    return god

def vyvod_resultata():
    print (god)

################################################################################

nomer_goda = vvod_dannyh()

god = raschet()

vyvod_resultata()
