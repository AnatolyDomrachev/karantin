def zap_massiva():
    f = open('slov_data2.txt', 'r')
    massiv = []
    y = {}
    for i in range(0,3):
        w = f.readline().replace('\n', '')
        x = w.split(':')
        y = {"university":x[0], "group":x[1]}
        massiv.append(y.copy())
    return (massiv)
def func(massiv, stroka):
    itog = []
    for i in massiv:
        if stroka == i["university"] or stroka == i["group"]:
            itog.append(i)
    return (itog)

m = zap_massiva()
print(m)
stroka = input("Введите строку: ")
result = func(m, stroka)
if result:
    print(result)
else:
    print(m)