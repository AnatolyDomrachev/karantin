n = int(input("Enter n: "))
fib1 = 1
fib2 = 1

print(fib1)
print(fib2)

for fib in range(1000):
    fib = fib1 + fib2
    print(fib)
    fib1 = fib2
    fib2 = fib


