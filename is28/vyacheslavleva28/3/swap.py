result=False
a=[1,3,5,6,7,6,54,6,4,5]

x = int(input("integer:"))

for i in range(len(a)):
    if a[i]==x:
        tmp = a[i]
        a[i] = a[0]
        a[0] = tmp

        break
print(a)

