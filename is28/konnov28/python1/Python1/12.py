n = int(input("Введите натуральное n: "))

f_prev = 1
f_prev_prev = 1

print("Число Фибоначчи под номером ", 0, " = ", 1)
if n > 0:
    print("Число Фибоначчи под номером ", 1, " = ", 1)

for i in range(2, n + 1):
    f_current = f_prev + f_prev_prev
    print("Число Фибоначчи под номером ", i, " = ", f_current)
    f_prev_prev = f_prev
    f_prev = f_current
