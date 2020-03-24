an=[]
print("Введите данные массива")
for i in range(10):
 x=int(input())
 an.append(x)
i=int(input("Введите число"))
if i in an:
 print("TRUE")
else:
 print("FALSE")