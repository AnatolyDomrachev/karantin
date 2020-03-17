

def vvod_dannyh():
    data = int(input("Введите целое число"))
    return data

def raschet(data):
    for i in range(len(l)):
        if l[i] == data:
            return True
    return False

def vyvod_resultata(res):
    print("встречается" if res else "не встречается")

l = [0,1,2,3,4,5,6,7,8,9]

data = vvod_dannyh()
res = raschet(data)
vyvod_resultata(res)




