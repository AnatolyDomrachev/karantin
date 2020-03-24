import math
s = int(input())
k = int(s % 10)
s = int(s // 10)
smm = k
k = int(s % 10)
s = int(s // 10)
smm = smm + k + s
print(smm)