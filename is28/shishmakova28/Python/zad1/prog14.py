print('Введите значение n')
N=int(input())
A=1
B=1
C=0
if N>=1:
	print(A)
	print(B)
else:print(0)
while A+B<=N:
	C=A+B
	print(C)
	A=B
	B=C