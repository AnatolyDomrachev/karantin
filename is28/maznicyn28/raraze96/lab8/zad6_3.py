a = []
f = open("pcp.txt", "r")
n = f.readline()
c = n.split(":")
b = {"name":c[0],"Id":c[1]}
f.close()
k = 1
namefile = input()
f = open(namefile, "r")
n = f.readline()
while n != "":
 c = n.split(":")
 l = {"name":c[0],"Id":int(c[1])}
 a.append(l.copy())
 n = f.readline()
 k += 1
f.close()
a.append(b)
f = open("output.txt", "w")
for i in range(0,k):
 f.write(a[i]["name"] + ":" + str(a[i]["Id"]) + "\n")
f.close()
