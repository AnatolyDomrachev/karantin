n = int(input("введите число n "))
a = False
for i in range(2,n):
    for j in range(2, int((i/2)+1)):
            if(i % j !=0): 
                a = True
            else:
                a = False
                break
    if(a == True):
        print(i)