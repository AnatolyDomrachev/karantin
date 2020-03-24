

f1=f2=1
s=0

while f2 < 1000:
	f_sum = f2 +f1
	f1 = f2
	f2=f_sum
	s=s+f1
	print(f1)
print(s)