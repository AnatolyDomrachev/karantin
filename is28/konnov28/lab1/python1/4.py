

def vvod_dannyh():
    data = []
    for i in range(10):
        data.append(float(input("ведите элемент под номером " + str(i) + ":")))
    return data

def raschet(data):
    for i in range(len(data)-1):
        if data[i] > data[i + 1]:
            return False
    return True

def vyvod_resultata(res):
    print("" if res else "не", "образуют возрастающую последовательность")

data = vvod_dannyh()
res = raschet(data)
vyvod_resultata(res)




