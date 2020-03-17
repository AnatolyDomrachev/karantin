
a = [[1,5,6,4],[3,2,15,8],[10,9,8,11],[14,16,11,17]]

max = a[0][0]
min = a[0][0]
for i in range(len(a)):
	for j in range(len(a[0])):
		if a[i][j] > max:
			max = a[i][j]
print(max)

for i in range(len(a)):
	for j in range(len(a[0])):
		if a[i][j] < min:
			min = a[i][j]	
print(min)

print(max-min)			


#ok