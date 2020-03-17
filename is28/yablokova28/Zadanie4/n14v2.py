def vvod_stroki():
	str = input()
	return (str)

def dstv_nad_strokoy(str):
	a = []
	dls = []
	a=str.split(" ")
	for i in range(len(a)):
		dls.append(len(a[i]))
	return (dls)

def vyvod(dls):
	print(dls)
	return()

a= vvod_stroki()
b= dstv_nad_strokoy(a)
vyvod(b)

