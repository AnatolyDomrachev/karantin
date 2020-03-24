f0 = 1
f1 = 1
f = 1

n = int(input("n: "))
for x in range(n):
  f = f0 + f1
  f0 = f1
  f1 = f  
  print(f)
  
  