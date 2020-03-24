n = int(input("Введите натуральное n: "))

f_prev = 1
f_prev_prev = 1
# хоть в задании и сказано, что n > 1но мы все равно обработаем такой случай
if n < 2:
    f_current = 1

for i in range(2, n + 1):
    f_current = f_prev + f_prev_prev
    f_prev_prev = f_prev
    f_prev = f_current


print("Число Фибоначчи под номером ", n, " = ", f_current)
