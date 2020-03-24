def digitCount(k):
    count = 0
    while k>0:
        count+=1
        k//=10
    return count


val = int(input("Введите целое число: "))
print("Количество цифр в ",val," = ",digitCount(val))