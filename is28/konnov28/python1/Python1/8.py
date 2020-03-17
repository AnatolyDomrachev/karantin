k = int(input("Введите натуральное k: "))

s = ""
i = 10

while len(s) < k:
    s = s + str(i) # s += str(i)
    i = i * 10  # i *= 10

print("Цифра последовательности под номером ", k, ":", s[k - 1])
