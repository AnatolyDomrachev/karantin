i=[1,2,3,4]
j=[5,3,2,6]
k=[4,3,5,2]
l=[2,3,4,5]
a=[i,j,k,l]
print("заполните матрицу")
a[0][0]= int(input("Введите число (1:1)" ))
a[0][1]= int(input("Введите число (1:2)" ))
a[0][2]= int(input("Введите число (1:3)" ))
a[0][3]= int(input("Введите число (1:4)" ))
a[1][0]=int(input("Введите число (2:1)" ))
a[1][1]=int(input("Введите число (2:2)" ))
a[1][2]=int(input("Введите число (2:3)" ))
a[1][3]=int(input("Введите число (2:4)" ))
a[2][0]=int(input("Введите число (3:1)" ))
a[2][1]=int(input("Введите число (3:2)" ))
a[2][2]=int(input("Введите число (3:3)" ))
a[2][3]=int(input("Введите число (3:4)" ))
a[3][0]=int(input("Введите число (4:1)" ))
a[3][1]=int(input("Введите число (4:2)" ))
a[3][2]=int(input("Введите число (4:3)" ))
a[3][3]=int(input("Введите число (4:4)" ))
print("до")
print(a[0][0],a[0][1],a[0][2],a[0][3])
print(a[1][0],a[1][1],a[1][2],a[1][3])
print(a[2][0],a[2][1],a[2][2],a[2][3])
print(a[3][0],a[3][1],a[3][2],a[3][3])
print("после")
n=a[0]
x=0
b=0
for i in range(3):
   if a[i][0]>b:
       a[0]= a[i]
       x=i
a[x]= n

print(a[0][0],a[0][1],a[0][2],a[0][3])
print(a[1][0],a[1][1],a[1][2],a[1][3])
print(a[2][0],a[2][1],a[2][2],a[2][3])
print(a[3][0],a[3][1],a[3][2],a[3][3])





       
    
