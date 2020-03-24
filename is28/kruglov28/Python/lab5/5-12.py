import random
data = open ('5-12-data.txt','r')
result = open ('5-12-result.txt','w')

M = [random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),
     random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),
     random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),
     random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)]

def vvod_dannyh():
    vvod=str(data.read())
    vvod=vvod.split(' ')
    return vvod

def raschet():
    M[j],M[k]=M[k],M[j]
    M[j+4],M[k+4]=M[k+4],M[j+4]
    M[j+8],M[k+8]=M[k+8],M[j+8]
    M[j+12],M[k+12]=M[k+12],M[j+12]
    return M

def vyvod_resultata():
    result.write (M)
    print ('Полученный результат был выведен в файл 5-12-result.txt')
    result.close()
    
#################################################


dannye = vvod_dannyh()#Ввод данных
j=int(dannye[0])-1
k=int(dannye[1])-1
print ("В сгенерированной матрице программа поменяет местами столбцы, номера которых указаны в файле 5-12-data.txt -",j+1,"и",k+1,"столбцы. Изначально программа сгенерировала следующую матрицу M:")
print ('\n',M[0],M[1],M[2],M[3],'\n',M[4],M[5],M[6],M[7],'\n',M[8],M[9],M[10],M[11],'\n',M[12],M[13],M[14],M[15],'\n')

if j<0 or j>3 or k<0 or k>3:
    result.write ("Столбцы с введёнными номерами в данной матрице отсутствуют.")
    result.close()
    print ("Столбцы с введёнными номерами в данной матрице отсутствуют.")
    raise SystemExit
else:
    M = str(raschet())    #Расчёт
    vyvod_resultata()    #Вывод результата
    
