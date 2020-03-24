k = int(input("k:"))
a = 1 
n = 0
posl = str()
while a == 1:
 n= n + 1
 stroka = n
 stroka = str(stroka)
 posl = posl+stroka 
 
 if n == k:
    a = 0
print(posl[k-1])