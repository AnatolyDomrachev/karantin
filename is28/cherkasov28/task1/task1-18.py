k = int(input("Введите число: "))
i = 1

n=9; prev = 0; i=0 

while n<k:
    i += 1
    prev = n
    n += ( 9*(10**i)  ) * (i+1)

if k<10:
    val = k
else:
    number = ((k - prev)-1)//(i+1)
    val = (10**i)+(number)

digit = (val // 10**(( (val)-( 10**(i) - 1 ) )*(i+1) + prev - k )) % 10

print("В заданной условиями последовательности на номером ",k," находится цифра ",digit)
