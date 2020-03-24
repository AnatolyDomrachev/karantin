def printFibonacchi(N):
    prev = 1; prev2 = 0; current = 0
    i=0

    while current<=N:
        print(i+1," - ",current)
        current = prev+prev2
        prev2 = prev
        prev = current
        

n = int(input("Введите число: "))
printFibonacchi(n)
