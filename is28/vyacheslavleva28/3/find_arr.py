result=False
a=[1,3,5,6,7,6,54,6,4,5]

x = int(input("integer:"))

for y in a:
    if y==x:
        result=True
        break
print(result)

