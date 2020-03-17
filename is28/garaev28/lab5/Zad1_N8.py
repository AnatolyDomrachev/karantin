k=int(input())
d='10'
s=2
while len(d)<1+k:
 d=d+str(10**s)
print(d[k-1])
#print(d)