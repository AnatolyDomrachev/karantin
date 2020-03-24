
def print_m(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end = "\t")
        print()



m = [
    [11,12,13,14],
    [21,22,23,24],
    [31,66,33,34],
    [41,42,43,44],
    ]


print_m(m)

row = 0
col = 0
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] > m[col][row]:
            row = i
            col = j

print("Максимум", m[col][row])
print("Строка", row)
print("Столбец", col)
