a = int(input(" введите возраст"))
if a>=10 and a<=20:
	print(a, "лет")
else:
	x = a%10
	if x == 1:
		print(a, "год")
	if x == 2 or x == 3 or x == 4:
		print(a, "года")
	if x>=5 and x<=9 or x == 0 :
		print(a, "лет")