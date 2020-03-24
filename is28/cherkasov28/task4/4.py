def isLeapyear(year):
    """Возвращает True, если год високосный и False в противном случае"""
    return bool( not (year%400) or ( not (year%4) and year%100 ) )

year = int(input("Введите номер года: "))
print("Год високосный: ",isLeapyear(year))