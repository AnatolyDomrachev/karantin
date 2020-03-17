n = int(input("Введите натуральное n: "))

def is_simple(k):
    for i in range(2, k):
        if k % i == 0:
            return False
    return True

print("Все простые числа из диапазона [ 2 ,", n, "]:")
for i in range(2, n + 1): # 2 <= i < n + 1
    if is_simple(i):
       print(i)
