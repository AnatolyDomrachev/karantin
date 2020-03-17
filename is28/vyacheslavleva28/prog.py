M = 4
N = 4

def read_matrix():
    print("Ввод матрицы")
    m = []
    for i in range(M):
        m.append([])
        for j in range(N):
            m[i].append(int(input()))
    return m

def f_min_str(m):
    res = []
    v = {}
    imin = 0
    jmin =0
    for i in range(M):
        mmin = m[i][0]
        imin = i

        for j in range(N):
            if m[i][j] < mmin:
                mmin = m[i][j]
                jmin =j

        v['val'] = mmin
        v['i'] = imin
        v['j'] = jmin
        res.append(v.copy())

    return res 

def f_min_stl(m):
    res = []
    v = {}
    imin = 0
    jmin =0
    for j in range(N):
        mmin = m[0][j]
        jmin =j

        for i in range(M):
            if m[i][j] < mmin:
                mmin = m[i][j]
                imin = i

        v['val'] = mmin
        v['i'] = imin
        v['j'] = jmin
        res.append(v.copy())

    return res 

def f_max_str(m):
    res = []
    v = {}
    imin = 0
    jmin =0
    for i in range(M):
        mmin = m[i][0]
        imin = i

        for j in range(N):
            if m[i][j] > mmin:
                mmin = m[i][j]
                jmin =j

        v['val'] = mmin
        v['i'] = imin
        v['j'] = jmin
        res.append(v.copy())

    return res 

def f_max_stl(m):
    res = []
    v = {}
    imin = 0
    jmin =0
    for j in range(N):
        mmin = m[0][j]
        jmin =j

        for i in range(M):
            if m[i][j] > mmin:
                mmin = m[i][j]
                imin = i

        v['val'] = mmin
        v['i'] = imin
        v['j'] = jmin
        res.append(v.copy())

    return res 


    return []

def f_points(a1 , a2):
    res = []
    for i in range(M):
        if a1[i] == a2[i]:
            res.append(a1.copy())
    return res

matrix = read_matrix()
for i in range(M):
    print(matrix[i])
print()
min_str = f_min_str(matrix)
for i in range(M):
    print(min_str[i])
print()
min_stl = f_min_stl(matrix)
for i in range(M):
    print(min_stl[i])
print()
max_str = f_max_str(matrix)
for i in range(M):
    print(max_str[i])
print()
max_stl = f_max_stl(matrix)
for i in range(M):
    print(max_stl[i])
print()
points1 = f_points(min_str, max_stl)
points2 = f_points(max_str, min_stl)

print(points1)
print(points2)

