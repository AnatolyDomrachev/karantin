def abv(pxp):
	a=[]
	f=open('pxp.txt', 'r')
	n=f.readline()
	while n!="":
		c=n.split("\t")
		b={"name":c[0],"ID":int(c[1])}
		a.append(b)
		n=f.readline()
	f.close()
	return a 
pxp=input();
print(abv(pxp));
