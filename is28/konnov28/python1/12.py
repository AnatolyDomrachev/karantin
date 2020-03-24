
def print_m(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end = "\t")
        print()



m = [
    [11,12,13,14],
    [21,22,23,24],
    [31,32,33,34],
    [41,42,43,44],
    ]

j = 0
k = 2

print("Было")
print_m(m)

for i in range(len(m)):
    temp = m[i][j]
    m[i][j] = m[i][k]
    m[i][k] = temp

print("Стало")
print_m(m)
