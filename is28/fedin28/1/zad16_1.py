a=int(input())
for i in range(2,a+1):
	isSimpleDigit = True
	for j in range(2,i):
		if i%j==0:
			isSimpleDigit = False
			break
	if isSimpleDigit:
		print(i)