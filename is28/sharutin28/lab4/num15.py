a = input()
list = a.split()
count = 2147483
for i in list:
	if len(i) < count:
		count = len(i)
		word = i
		
print(word)		
