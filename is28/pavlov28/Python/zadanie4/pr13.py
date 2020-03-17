def func():
	string = input("Введите строкy со словами: ")
	maxlen = 0
	for i in string.split(" "):
		if len(i) > maxlen:
			maxlen = len(i)
	return maxlen
	
stri = func()
print(stri)	