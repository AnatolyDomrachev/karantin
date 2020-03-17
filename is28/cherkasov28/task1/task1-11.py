def fibonacchi(k):
    prev = 1; prev2 = 0; current = 0

    for i in range(1,k):
        current = prev+prev2
        prev2 = prev
        prev = current
    return current

n = int(input("Введите номер числа фибоначи, которое вы хотите вычислить: "))
print("Число фибоначчи под номером ",n," = ",fibonacchi(n))