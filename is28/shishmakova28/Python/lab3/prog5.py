print('Введите день недели')
A=int(input())
B=A+1//7
print(not bool(B%2==0 or (A%7==0 and B%2==0)))