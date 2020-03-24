i = int(input())
k = int(input())

a = [[1,5,6,4],[3,2,15,8],[10,9,8,11],[14,16,11,17]]

print(a)

a[i],a[k] = a[k],a[i]

print(a)