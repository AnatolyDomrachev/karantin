a=int(input("Сколько вам лет = "))
if a%10 == 1:
	print(a,"год")
elif a%10 > 1 and a%10 < 5:
	print(a,"года")
else:
	print(a,"лет")