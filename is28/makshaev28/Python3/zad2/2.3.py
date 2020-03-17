import random

N=10
massiv=[random.randint (1, 100) for i in range(N)]


k=int(input("Введите проверяемое число:"))
print()
for i in massiv:
 if k in massiv:
  print("Число есть в массиве")
  break
 else:
  print("Числа нет в заданном массиве")
  break

print()  
print ('Старый массив:',massiv)
print()
massiv.append( int(k))
print("Строим новый массив")
print()
print('Новый массив после ввода числа:',massiv)
 
