def vvod_dannyh():
    print("Введите строку. Программа выведет первое из самых коротких слов в ней.")
    vvod = str(input())
    return vvod

def process():
    IDshort = 0
    for m in range(len(dannye)):
        if len(dannye[m])<len(dannye[IDshort]):
            IDshort = m
    return IDshort

def vyvod_resultata():
    print(dannye[IDshort])

################################################################################

dannye = vvod_dannyh()
dannye = dannye.split()

IDshort = process()

vyvod_resultata()
