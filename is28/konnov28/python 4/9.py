
def remove(s, n, m):
    return s[:n] + s[n + m:]

s = "Питон велик! Питон слаб... ой! Питон могуч!"
n = 12
m = 18

print("Было:", s)
print("Стало:", remove(s, n, m))
