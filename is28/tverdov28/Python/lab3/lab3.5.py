k = int(input("Введите номер дня"))
n = k % 7 +1
print(not bool(n%2==0 or (k%7==0 and (k//7)%2==0)))