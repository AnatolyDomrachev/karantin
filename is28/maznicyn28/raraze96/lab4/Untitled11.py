a = int(input())
x = 1
y = 1
for i in range(2,a + 1):
 x,y = y,x
 x = x + y
print(x)
 