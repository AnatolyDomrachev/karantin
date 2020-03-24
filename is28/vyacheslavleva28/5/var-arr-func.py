def qwe(a):
    a += 1

def qwer(a):
    a[0] += 1

print("Для переменной")
a=3
qwe(a)
print(a)


print("Для массива")
a=[3]
qwer(a)
print(a)

