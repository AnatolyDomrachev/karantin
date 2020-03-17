n = int(input("Введите число n: "))

s = ""
i = n

while i > 0:
    s = str(i % 2) + s
    i = i // 2

if n == 0:
    s = "0"

print("В двоичной записи числа ", n, "содержится цифр:", len(s))
