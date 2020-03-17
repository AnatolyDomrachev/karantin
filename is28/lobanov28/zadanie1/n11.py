n = int(input("введите n"))
fib1=fib2=1
k=0
while k < n-2:
	fib_sum = fib2 +fib1
	fib1 = fib2
	fib2=fib_sum
	k = k+1
print(fib2)	



