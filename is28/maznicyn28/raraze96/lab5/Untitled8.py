b = []
c = 0;
for i in range(0,10):
 b.append(float(input()))
if b[0] > b[1] or b[0] < b[1]:
 c += 1;
for i in range(1,9):
 if b[i] > b[i - 1] or b[i] > b[i + 1] or b[i] < b[i - 1] or b[i] < b[i + 1]:
  c += 1;
if b[8] > b[9] or b[8] < b[9]:
 c += 1;
print(c)
   
