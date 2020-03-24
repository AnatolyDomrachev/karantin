x=str(input("number:"))
y = len(x)
u = y
res = str()
for i in range(y):
 res= res + str(x[u-1])
 u = u-1
 
if x == res:
 print("палиндром")
else:
  print("Не палиндром")
