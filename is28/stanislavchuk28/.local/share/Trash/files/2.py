a=[]
M=4
N=4
for i in range(M):
    a.append([])
    for j in range(N):
        a[i].append(input())
print(a)
rows_cnt=len(a)
cols_cnt=len(a[0])
new_a=[[0]*rows_cnt for_in range(cols)cnt)]
for i in range(rows_cnt):
	for j in range(cols_cnt):
		new_a[j][i]=a[i][j]
for row in new_a:
	print(row)
		