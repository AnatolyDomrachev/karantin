def vvod_dannyh(): 
    print("Ввод исходных данных") 
    vvod=[] 
    for i in range(0,3): 
        vvod.append(input()) 
    return vvod 
	
def raschet(data):
	print("get: ",data)

#главный модуль 
dannye = vvod_dannyh() 
raschet(dannye)
