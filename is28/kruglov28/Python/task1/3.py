a = int(input("Введите порядковый номер месяца - "))
if a > 0:
    if a > 11:
        a = a-(a//12)*11-(1*a//12)
    else:
        a = a
    S = a//3+1
    if S == 1:
        print("Введённый Вами месяц - месяц зимы.")
    elif S == 2:
        print("Введённый Вами месяц - месяц весны.")
    elif S == 3:
        print("Введённый Вами месяц - месяц лета.")
    else:
        print("Введённый Вами месяц - месяц осени.")
else:
    print("Порядковый номер месяца не может быть меньше или равен нулю.")
