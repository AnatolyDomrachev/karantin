

x = [1.,2.,3.,4.,5.]
y = [1.1,2.1,3.1,4.1,5.1]
z = [1.2,2.2,3.2,4.2,5.2]

xmin = x[0]
ymin = y[0]
zmin = z[0]

for i in range(1,5):
    if xmin > x[i]:
        xmin = x[i]
    if ymin > y[i]:
        ymin = y[i]
    if zmin > z[i]:
        zmin = z[i]

if xmin > ymin:
    if xmin > zmin:
        print("x:", x)
    else:
        print("z:", z)
else:
    if ymin > zmin:
        print("y:", y)
    else:
        print("z:", z)
