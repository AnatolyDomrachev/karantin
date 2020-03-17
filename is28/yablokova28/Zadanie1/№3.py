x=input("Введите номер месяца ")
x=int(x)
if 1<=x<=2 or x==12:
    print("Зима")
elif 3<=x<=5:
    print("Весна")
elif 6<=x<=8:
    print("Лето")
elif 9<=x<=11:
    print("Осень")