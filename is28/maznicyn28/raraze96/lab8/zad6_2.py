a = []
b = {}
f = open("pxp.txt","r")
for i in range (0,5):
 v = f.readline()
 ar = v.split(":")
 c = ar[1]
 n = int(len(c))
 l = ""
 for j in range(0,n-1):
  l = l + c[j]
 print(l)
 b = {"first": ar[0],"second":l}
 a.append(b.copy())
g = input()
if (g == ""):
 print(a)
for i in range(0,5):
 if (g == a[i]["first"]) or (g == a[i]["second"]):
  print(a[i])
 
