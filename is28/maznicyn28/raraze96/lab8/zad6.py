def abvdeyog(pxp):
 a = []
 f = open(pxp, 'r')
 n = f.readline()
 while n != "":
  c = n.split(":")
  b = {"name":c[0],"Id":int(c[1])}
  a.append(b)
  n = f.readline()
 f.close()
 return a
pxp = input();
print(abvdeyog(pxp));	
  