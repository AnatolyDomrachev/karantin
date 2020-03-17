import random

def vvod_massiva (text):
	a=[]
	f = open(text, 'r')
	a = f.read()
	return(a)

#def poisk_maximuma (massiv):
#	maximum = 0
#	for i in range (4):
#		if massiv[i][0] > maximum:
#			maximum = massiv[i][0]
#			index = i
#	massiv[0], massiv[index] = massiv[index], massiv[0]
#	return(massiv)
#
#def vyvod_massiva(massiv):
#	for i in range (4):
#		print(massiv[i])
#	return()
	
m = input() #ввод имени файла
m = vvod_massiva(m)
print(m)
#for i in range (4):
#	print(m[i])
#sw_mstrk = poisk_maximuma(m)
#print()
#vyvod_massiva(sw_mstrk)
