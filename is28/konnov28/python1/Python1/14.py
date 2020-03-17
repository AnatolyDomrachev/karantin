n = int(input("Введите натуральное n: "))

if n >= 1:
    print("Число Фибоначчи под номером ", 0, " = ", 1)
    print("Число Фибоначчи под номером ", 1, " = ", 1)

i = 2
f_prev = 1
f_prev_prev = 1
f_current = 2
while f_current <= n:
    print("Число Фибоначчи под номером ", i, " = ", f_current)
    i = i + 1
    f_prev_prev = f_prev
    f_prev = f_current
    f_current = f_prev + f_prev_prev
