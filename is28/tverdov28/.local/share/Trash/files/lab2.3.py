a = int(input("Ввести номер дня в годy, от 1 до 365"))
pn = 1; v = 2; sr = 3; ch = 4; p = 5; sb = 6; vs = 0;
for a in range (1, 366):
  if a % 7 == 0:
   print("воскресенье")
  if a % 7 == 1:
   print("понедельник")
  if a % 7 == 2:
   print("вторник")
  if a % 7 == 3:
   print("среда")
  if a % 7 == 4:
   print("четверг")
  if a % 7 == 5:
   print("пятница")
  if a % 7 == 6:
   print("сyббота")
   
  