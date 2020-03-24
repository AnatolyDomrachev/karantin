 
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


print_m(m)

max = m[0][0]
min = m[0][0]
for i in range(len(m)):
    for j in range(len(m[i])):
        if m[i][j] < min:
            min = m[i][j]
        if m[i][j] > max:
            max = m[i][j]
        

print("Минимум", min)
print("Максимум", max)
print("Разность", max - min)
