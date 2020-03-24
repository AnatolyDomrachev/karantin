def poisk(str1):
	str2 = input("Введите искомyю строкy: ")
	stro = str1.find(str2)
	if stro > 0: 
		result = True
	else:
		result = False
	return result
	








str1 = input("Введите начальнyю строкy: ")
result = poisk(str1)
print(result)
