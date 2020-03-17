print('Введите целое число')
A=int(input())
K=0
while A//2!=0:
	K=K+1
	A=A//2
print(K+1)