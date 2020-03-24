

def vvod_dannyh():
    n = int(input("Введите длинну массива:"))
    data = []
    for i in range(n):
        data.append(input("ведите элемент под номером " + str(i) + ":"))
    return data

def raschet(data):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data [j]:
                return True
    return False

def vyvod_resultata(res):
    print("есть" if res else "нет")

data = vvod_dannyh()
res = raschet(data)
vyvod_resultata(res)




