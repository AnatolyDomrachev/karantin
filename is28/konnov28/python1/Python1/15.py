f_prev = 1
f_prev_prev = 1
f_current = 2
s = 2

lim = 13
while f_current <= lim:
    s = s + f_current
    f_prev_prev = f_prev # 1
    f_prev = f_current # 2
    f_current = f_prev + f_prev_prev

print("Сумма всех чисел Фибоначчи не превосходящих", lim, "равна", s)
