import random
from random import randint
K = randint(1,10)
A = [randint(0,101) for x in range (K)]
print ("В этот раз количество элементов в массиве равно", K,"; программа сгенерировала следyющий массив:")
print (A)
i = 0
a = 0
while i < K:
	a = a + A[i]
	i = i +1
print ("Среднее арифметическое элементов массива равно",a/K)
