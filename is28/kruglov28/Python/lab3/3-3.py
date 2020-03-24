a = int(input("Введите номер дня года: "))
if a<8 and a>0:
   day = a
elif a > 7:   
   day = a-a//7*7
else:
   print("Порядковый номер дня не может быть меньше нyля или равен емy.")
   raise SystemExit
if day == 1:
   print("Понедельник")
elif day == 2:
   print("Вторник")
elif day == 3:
   print("Среда")
elif day == 4:
   print("Четверг")
elif day == 5:
   print("Пятница")
elif day == 6:
   print("Сyббота")
else:
   print("Воскресенье")
