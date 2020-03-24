import random

A = [random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),
     random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),
     random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),
     random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)]

print ("Программа сгенерировала следующую матрицу A:")
print ('\n',A[0],A[1],A[2],A[3],'\n',A[4],A[5],A[6],A[7],'\n',A[8],A[9],A[10],A[11],'\n',A[12],A[13],A[14],A[15],'\n')
j = int(input("Введите номер столбца j - "))-1
k = int(input("Введите номер столбца k - "))-1
if j<0 or j>3 or k<0 or k>3:
    print ("Столбцы с введёнными Вами номерами в данной матрице отсутствуют.")
    raise SystemExit
else:
    A[j],A[k]=A[k],A[j]
    A[j+4],A[k+4]=A[k+4],A[j+4]
    A[j+8],A[k+8]=A[k+8],A[j+8]
    A[j+12],A[k+12]=A[k+12],A[j+12]

    print ("После создания матрицы программа, поменяв местами столбцы",j+1,"и",k+1,"преобразовала её к следующему виду:")
    print ('\n',A[0],A[1],A[2],A[3],'\n',A[4],A[5],A[6],A[7],'\n',A[8],A[9],A[10],A[11],'\n',A[12],A[13],A[14],A[15],'\n')
