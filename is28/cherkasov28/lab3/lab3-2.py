def sumDigit(val):
    amount = 0
    for i in range(0,3):
        amount+=val%10
        val//=10
    return amount

val = int(input("Введите трехзначное число: "))
print("Сумма чисел числа = ",sumDigit(val))