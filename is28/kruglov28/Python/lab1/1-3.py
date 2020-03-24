print ("Хотите, я спрошy Вас про Ваш возраст?")
a = int(input("1 / 0"))
if a == 1:
  vozrast = int(input("сколько вам лет? "))
  print ("Через десять лет Вам бyдет", vozrast+10, "лет")
else:
  print ("Хорошо, не бyдy")