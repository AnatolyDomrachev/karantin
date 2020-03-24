import itertools

def deleteRepeatingElements(arr):
    """Удаляем повторяющиеся элементы в списке"""
    return [ a for a, _ in itertools.groupby(arr)]

def getCharsList(str1,str2):
    """Получаем список из символов, которые встречаются и в str1 и в str2"""
    charsList = []
    for char in str1:
        for char2 in str2:
            if char == char2:
                charsList.append(char)
    return deleteRepeatingElements(charsList)

str1 = input("Введите первую строку: ")
str2 = input("Введите вторую строку: ")
charList = getCharsList(str1,str2)
print("Элементы, которые есть и в первой и второй строках:\n",charList)