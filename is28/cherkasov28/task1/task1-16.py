def isSimple(k):
    count = 0
    for i in range(1,k+1):

        if(not k%i):
            count+=1

        if(count>2):
            return False

    return True

n = int(input("Введите число: "))
for i in range(2,n+1):
    if(isSimple(i)):
        print(i)
