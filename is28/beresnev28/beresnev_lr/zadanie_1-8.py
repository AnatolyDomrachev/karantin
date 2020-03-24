k=int(input("введите позицию числа = "))
x=""
for j in range(1,10):
	x=x+str(10**j)
x=list(x)
print(x[k-1])