h = []
for i in range(0,10):
	temp = float(input(''))
	h.append(temp)
for i in range(9):
	if h[i] < h[i+1]:
		a = True
	else:
		a = False
		break
print(a)
	