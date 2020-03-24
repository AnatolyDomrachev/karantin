k = int(input("Введите натуральное k: "))

s = ""
i = 1

while len(s) < k:
    s = s + str(i) # s += str(i)
    i = i + 1 # i++ # i += 1

print("Цифра последовательности под номером ", k, ":", s[k - 1])
