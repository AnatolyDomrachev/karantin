import math
d = int(input())
if 365 % d == 0:
	print('1 пн')
elif 365 % d == 1:
	print('2 вт')
elif 365 % d == 2:
	print('3 ср')
elif 365 % d == 3:
	print('4 чт')
elif 365 % d == 4:
	print('5 пт')
elif 365 % d == 5:
	print('6 сб')
else :
	print('7 вс')
	