b = []
k = 0
for i in range(0,10):
 b.append(float(input()))
c = int(input())
for i in range(0,10):
 if b[i] == c:
  k += 1
if k > 0:
 print("встречается")
else:
 print("невстречается")
