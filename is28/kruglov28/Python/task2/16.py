import random

A = [random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),
     random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),
     random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),
     random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)]
c=0

print ("Программа сгенерировала следующую матрицу A:")
print ('\n',A[0],A[1],A[2],A[3],'\n',A[4],A[5],A[6],A[7],'\n',A[8],A[9],A[10],A[11],'\n',A[12],A[13],A[14],A[15],'\n')
strok = int(input("Введите номер строки - "))-1
stolb = int(input("Введите номер столбца - "))-1

if -1<strok<4 and -1<stolb<4:
    #Избавляемся от строки
    while c<4:
        A.pop(strok*4)
        c+=1
    c=0
    #Избавляемся от столбца
    while c<3:
        A.pop(stolb+8-4*c)
        c+=1
else:
    print ("Столбцы с введёнными Вами номерами в данной матрице отсутствуют.")
    raise SystemExit

print ("Программа преобразовала матрицу A, удалив",strok+1,"строку и",stolb+1,"столбец:")
print ('\n',A[0],A[1],A[2],'\n',A[3],A[4],A[5],'\n',A[6],A[7],A[8],'\n')


