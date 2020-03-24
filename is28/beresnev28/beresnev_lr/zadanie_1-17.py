k=str(input("введите число = "))
f=list(k)
a=len(k)
r=0
for h in range(a):
	f[h]=int(f[h])
for g in range(a):
	if f[g] == f[(a-1)-g]:
		r=r+1
if r == a:
	print("число полиндром")
else:
	print("число не полиндром")