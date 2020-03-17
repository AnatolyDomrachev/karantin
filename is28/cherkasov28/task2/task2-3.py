import random

a = [random.randint(0,999999) for i in range(0,10)]
print("Массив: ",a)
k = int(input("Введите число: "))

print("Число ",k," встречается в массиве: ",k in a)