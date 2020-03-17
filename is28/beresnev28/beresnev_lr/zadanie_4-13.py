def input_k():
	k=0
	sr=str(input('sr='))+" "
	b=[]
	for i in sr:
		k+=1
		if i == " ":
			b.append(k-1)
			k=0
	return(b)
	
def sort_b(b):
	for j in range(len(b)-1):
		if b[j] < b[j+1]:
			d=b[j+1]
	return b[0]
b=input_k()
print(b)
p=sort_b(b)
print(p)
