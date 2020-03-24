def deleteExcessSpace(str1):
    return ' '.join(str1.split())

str1 = input("Введите строку: ")
print(deleteExcessSpace(str1))
