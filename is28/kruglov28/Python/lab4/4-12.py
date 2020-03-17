def vvod_dannyh():
    print("Введите строку, программа удалит из текста лишние пробелы.")
    vvod = list(input())
    return vvod

def process():
    n=0
    for i in range(len(dannye)-1):
        if dannye[n]==' ' and dannye[n]==dannye[n+1]:
            dannye.pop(n)
        else:
            n+=1
    return dannye

def vyvod_resultata():
    print(otvet)
    
################################################################################

dannye = vvod_dannyh()
otvet = "".join(process())
vyvod_resultata()
