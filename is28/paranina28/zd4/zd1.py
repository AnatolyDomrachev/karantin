
def asr(m,x):
 a = -1
 for i in range(0,5):
  if (m[i] == x):
   a = i
   break
 return a
m = [1,2,3,4,2]
x = 2
print(asr(m,x))

