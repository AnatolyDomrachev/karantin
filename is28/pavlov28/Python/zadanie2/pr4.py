a=[]
st = 0
for i in range (10):
	a.append(float(input())) 
for i in range (9):
	if a[i] > a[i+1]:
		st = 1
if st == 0:
	print("True")
else:
	print('False')
		
	
	
  
  
