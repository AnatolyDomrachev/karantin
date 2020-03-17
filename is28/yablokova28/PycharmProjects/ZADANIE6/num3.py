def func(name_file):
    f = open(name_file, "r")
    massiv = []

    for i in range(3):
        w = f.readline().replace('\n', '')
        x = w.split(':')
        y = {"university": x[0], "group": x[1]}
        massiv.append(y.copy())

    s = input('university')
    p = input('group')
    y = {'university':s, 'group':p}
    massiv.append(y.copy())
    f = open('slov_data3.txt', 'w')
    print(massiv, file=f)
    return (massiv)
data = input()
itog = func(data)