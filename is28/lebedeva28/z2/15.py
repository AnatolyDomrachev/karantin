M = 5
N = 5



print("Ввод матрицы")
matrix = []
for i in range(M):
	matrix.append([])
	for j in range(N):
		matrix[i].append(int(input()))
res = []
v = {}
imin = 0
jmin =0
for i in range(M):
	mmin = matrix[i][0]
	imin = i
	for j in range(N):
		if matrix[i][j] < mmin:
			mmin = m[i][j]
			jmin =j
	v['val'] = mmin
	v['i'] = imin
	v['j'] = jmin
	res.append(v.copy())
f_min_str=res



res1 = []
v1 = {}
imin = 0
jmin =0
for j in range(N):
	mmin = m[0][j]
	jmin =j
	for i in range(M):
		if matrix[i][j] < mmin:
			mmin = matrix[i][j]
			imin = i
	v1['val'] = mmin
	v1['i'] = imin
	v1['j'] = jmin
	res1.append(v1.copy())
f_min_stl=res1



res2 = []
v2 = {}
imin = 0
jmin =0
for i in range(M):
	mmin = matrix[i][0]
	imin = i
	for j in range(N):
		if matrix[i][j] > mmin:
			mmin = matrix[i][j]
			jmin =j
	v2['val'] = mmin
	v2['i'] = imin
	v2['j'] = jmin
	res2.append(v2.copy())
f_max_str=res2



res3 = []
v3 = {}
imin = 0
jmin =0
for j in range(N):
	mmin = matrix[0][j]
	jmin =j
	for i in range(M):
		if matrix[i][j] > mmin:
			mmin = matrix[i][j]
			imin = i
	v3['val'] = mmin
	v3['i'] = imin
	v3['j'] = jmin
	res3.append(v3.copy())
f_max_stl=res3




res4 = []
for i in range(M):
	if f_min_str[i] == f_max_stl[i]:
		res4.append(f_min_str.copy())
points1=res4		
	    
	    
res5 = []
for i in range(M):
	if f_max_str[i] == f_min_stl[i]:
		res5.append(f_max_str.copy())
points2=res5



print(res4)
print(res5)
