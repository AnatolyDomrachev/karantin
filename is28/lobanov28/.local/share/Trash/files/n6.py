n = int(input("введите чилсо"))
b= ''
while n > 0:
    b = str(n % 2) + b
    n = n // 2
 
print("количество цифр в двоичной системе: ", len(b))