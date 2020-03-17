import random

def vvod():
	N=int(input())
	arr=[]
	for i in range(N):
		arr.append(random.randint(0, 100))
	return(arr)

def raschet(arr):
	y=-1
	x=int(input())
	for i in range(len(arr)):
		if arr[i]==x:
			y=i
			break
	return(y)		
	
def vyvod(res):
	print(res)
	
	
arr=vvod()
print(arr)
res=raschet(arr)
vyvod(res)