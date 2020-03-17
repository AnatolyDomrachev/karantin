#def input_arr(x):
#	a=[]
#	f=open(x,"r")
#	for i in range (5):	
#		y=f.readline()
#		b={x:y}
#		a.append(b)
#	f.close()
#	return a

def input_arr(x):
	a=[]
	f=open(x,"r")
	y=f.readline()
	while y!="":
		z=y.split(":")
		b={"name":z[0],"id":int(z[1])}
		a.append(b)
		y=f.readline()
	f.close()
	return a


x=input()
print(input_arr(x))
