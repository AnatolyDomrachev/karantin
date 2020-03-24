import random
N = random.randint(0,1000001)

a = 0
b = 1
c = 0
print("Числом N, которое не будут превышать выведенные числа Фиббоначчи,",'\n',"рандом избрал число ",N,". Числа последовательности, удовлетворяющие условию:",sep="")
print()
while c < N:
    if a + b < N:
        c = a + b
        a = b
        b = c
        print(b)
    else:
        raise SystemExit

