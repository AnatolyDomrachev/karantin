seasons = ["Зима","Весна","Лето","Осень"]
val = int(input("Введите номер текущего месяца: "))
if val == 12:
    val = 1
print("Сейчас ",seasons[(val) // 3])