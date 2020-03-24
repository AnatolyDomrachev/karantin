def getTwoDegree(k):
    i=0
    while k >= 2**i:
        i+=1
    return i

val = int(input("Введите целое неотрицательное число: "))
print("Символов требуется для двоичного представления числа ",val," потребуется %d " %getTwoDegree(val))
