def calculateFibonacchiAmount():
    prev = 1; prev2 = 0; current = 0   
    amount = 0
    while current<=100:
        amount += current
        current = prev+prev2
        prev2 = prev
        prev = current
        
    return amount

print("Сумма чисел фибоначчи(только положительные индексы) с значениями не превышающих 100 = ",calculateFibonacchiAmount())