n=int(input())
summa=0
while n>0:
	if n%10!=0:
		summa=summa+n%10
		n=n//10
print(summa)
