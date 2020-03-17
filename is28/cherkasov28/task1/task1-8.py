def getTenDigree(k):
    i = 2
    digitAmount = 2
    while digitAmount <= k:
        i+=1
        digitAmount = (i*(i+1))//2 - 1
    return i-1, ( ((i)*(i+1) )//2 - 1 ) - k

k = int(input("Введие k: "))
tenDigree, digitNumber = getTenDigree(k)
print("В заданной условиями последовательности по номером ",k, " находится цифра ",( 10**tenDigree // 10**digitNumber ) % 10)