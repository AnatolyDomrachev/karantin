a = [0,0,0,0,0,0,0,0,0,0]
b=0
for i in range(0,10):
   a[i]=int(input("введите число массива"))
x = int(input("введите искомое число"))   
for i in range(0,10):
   if a[i] == x:
      print("число ",x," eсть в массиве")
      b=1
      break
   
if b<1:
   print("такого числа нет в массиве")
