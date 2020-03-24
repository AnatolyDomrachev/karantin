
a=[]
b={}
min_str=[]
max_str=[]
min_stl=[]
max_stl=[]

M=5
N=5
for i in range(M):
    a.append([])
    for j in range(N):
        a[i].append(0)

for i in range(M):
    for j in range(N):
        a[i][j] = int(input())

for i in range(M):
    for j in range(N):
        print(a[i][j], end = '\t')
    print()
	
min = a[0][0]
max = a[0][0]

for i in range(M):
	mini = a[i][0]
	imin=i
	jmin =0
	for j in range(N):
		if a[i][j] < mini:
			mini = a[i][j]
			jmin = j
			imin =i
	b['val']=mini
	b['i']=imin
	b['j']=jmin
	min_str.append(b.copy())

for j in range(N):
	mini = a[0][j]
	imin=0
	jmin =j
	for i in range(M):
		if a[i][j] < mini:
			mini = a[i][j]
			jmin = j
			imin =i
	b['val']=mini
	b['i']=imin
	b['j']=jmin
	min_stl.append(b.copy())

print(min_str)
print()
print(min_stl)

for i in range(M):
	maxi = a[i][0]
	imax=i
	jmax =0
	for j in range(N):
		if a[i][j] > maxi:
			maxi = a[i][j]
			jmax = j
			imax =i
	b['val']=maxi
	b['i']=imax
	b['j']=jmax
	max_str.append(b.copy())
  
for j in range(N):
	maxi = a[0][j]
	imax=0
	jmax =j
	for i in range(M):
		if a[i][j] > maxi:
			maxi = a[i][j]
			jmax = j
			imax =i
	b['val']=maxi
	b['i']=imax
	b['j']=jmax
	max_stl.append(b.copy())

print()        
print(max_str)
print()
print(max_stl)

for i in range(M):
	if min_str[i]['i'] == max_stl[i]['i'] and min_str[i]['j'] == max_stl[i]['j']:
		print("i=",min_str[i]['i'] , " j=",min_str[i]['j'])

for i in range(M):
	if max_str[i]['i'] == min_stl[i]['i'] and max_str[i]['j'] == min_stl[i]['j']:
		print("i=",min_str[i]['i'] , " j=",min_str[i]['j'])
	
    

