def zap_massiva(name_file):
    f = open(name_file, 'r')
    massiv = []
    for i in range(0,3):
        w = f.readline().replace('\n', '')
        x = w.split(':')
        y = {"university":x[0], "group":x[1]}
        massiv.append(y.copy())
    return (massiv)

data = input()
m = zap_massiva(data)
print(m)