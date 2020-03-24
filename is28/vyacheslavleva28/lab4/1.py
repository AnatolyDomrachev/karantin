k = int(input())

res = 0
x=1
a=2
while x<=k:
    print(x)
    if x == k:
        res = 1
    x+=a
    a+=1
print(res)

