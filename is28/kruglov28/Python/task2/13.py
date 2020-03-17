import random

A = [random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),
     random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),
     random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9),
     random.randint(0,9),random.randint(0,9),random.randint(0,9),random.randint(0,9)]


print ("Программа сгенерировала следующую матрицу A:")
print ('\n',A[0],A[1],A[2],A[3],'\n',A[4],A[5],A[6],A[7],'\n',A[8],A[9],A[10],A[11],'\n',A[12],A[13],A[14],A[15],'\n')
C=15
c=1
while C>0:
    if C!=12 and C!=8 and C!=4:
        A[C]*=-1
        C-=1
    else:
        C-=1
c=4
sh=0 
nA = max (A[4],A[8],A[12])
A[0]*=-1
iA = A.index (nA)
A[0]*=-1
while c>0:
    A[0+sh],A[iA+sh]=A[iA+sh],A[0+sh]
    sh+=1
    c=c-1
while C<16:
    if C!=12 and C!=8 and C!=4 and C!=0:
        A[C]*=-1
        C+=1
    else:
        C+=1
print ("После создания матрицы программа, поменяв местами первую строку и строку с наибольшим первым элементом с наименьшим индексом, преобразовала её к следующему виду:")
print ('\n',A[0],A[1],A[2],A[3],'\n',A[4],A[5],A[6],A[7],'\n',A[8],A[9],A[10],A[11],'\n',A[12],A[13],A[14],A[15],'\n')
