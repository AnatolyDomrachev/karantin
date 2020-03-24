def printFibonacchi(k):
    prev = 1; prev2 = 0; current = 0

    for i in range(0,k):
        print(i+1," - ",current)
        current = prev+prev2
        prev2 = prev
        prev = current
        

n = int(input("Введите номер числа фибоначи: "))
printFibonacchi(n)