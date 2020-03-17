
def visokos(y):
    if (y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0):
        return 1
    else:
        return 0

y = 1900
r = visokos(y)
print("Год номер", y, "високосный" if r == 1 else "не високосный")

y = 2000
r = visokos(y)
print("Год номер", y, "високосный" if r == 1 else "не високосный")
