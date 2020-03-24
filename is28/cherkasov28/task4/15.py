def getMinimalWordSize(str1):
    return min([ len(word) for word in str1.split()])

str1 = input("Введите строку: ")
print("Длинна самого короткого слова в строке: ",getMinimalWordSize(str1))