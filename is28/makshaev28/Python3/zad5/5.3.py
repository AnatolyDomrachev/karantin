k=int(input("Введите число:"))

def vvod_dannyh(): 
 f = open('data1.txt', 'r')
 vvod = [];
 for i in range(10):
   n = int(f.readline())
        
   vvod.append(n)
 return vvod
    

def raschet(vvod):
 n=dannye
 for i in n:
  if k in n:
   print("Число есть в массиве")
   break
  else:
   print("Числа нет в массиве")
   break

def vyvod_resultata(vvod):
 mt=dannye
 mt.append(k)
 f=open('result1.txt','w') #открытие в режиме записи
 f.write(str(mt))   # Запись  mt в файл
 f.close
 return mt




dannye = vvod_dannyh() 

new=raschet(dannye)

mt=vyvod_resultata(dannye)
print('Новый массив:', mt)


