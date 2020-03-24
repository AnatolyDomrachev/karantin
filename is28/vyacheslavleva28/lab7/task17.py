
def func(strc, clv):
	col2 = 0
	
	for i in range(len(strc)-len(clv)):
		col = 0
		for j in range(len(clv)):
			if clv[j] == strc[i+j]:
				col +=1
		if col == len(clv):
			col2 += 1
	return col2

strc = input()
clv = input()
res = func(strc, clv)
print(res)