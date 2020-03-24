n = int(input("введите n"))
f1=f2=1
k=0
while k < n-2:
	f_sum = f2 +f1
	f1 = f2
	f2=f_sum
	k = k+1
print(f2)
