def asr(m,x):
 a = 0
 for i in range(0,5):
  if (m[i] == x):
   a = a+1
 return a
m = [1,2,3,2,5]
x = 2
print(asr(m,x))
